"""install.sh waits for SLES PAYG cloud registration before installing packages.

Runs install.sh's own wait_for_zypper_repos with fake systemctl / zypper on
PATH, so the bash that ships is the bash under test.
"""
from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INSTALL_SH = ROOT / "install.sh"


def _function(name: str) -> str:
    text = INSTALL_SH.read_text()
    m = re.search(rf"^{name}\(\) \{{\n.*?^\}}\n", text, re.S | re.M)
    assert m, f"{name} not found in install.sh"
    return m.group(0)


def _run(tmp_path: Path, *, cloud: bool, repos_after: int) -> tuple[subprocess.CompletedProcess, int]:
    """repos_after: zypper lr -E succeeds from this call on (0 = never)."""
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    calls = tmp_path / "calls"
    calls.write_text("")
    (bin_dir / "systemctl").write_text(
        "#!/bin/bash\n"
        + ("echo 'guestregister.service enabled'\n" if cloud else "")
    )
    (bin_dir / "zypper").write_text(
        "#!/bin/bash\n"
        f"echo x >> {calls}\n"
        f"n=$(wc -l < {calls})\n"
        f"[[ {repos_after} -gt 0 && $n -ge {repos_after} ]] && exit 0\n"
        "exit 6\n"
    )
    (bin_dir / "sleep").write_text("#!/bin/bash\nexit 0\n")
    for f in bin_dir.iterdir():
        f.chmod(0o755)
    env = {**os.environ, "PATH": f"{bin_dir}:/usr/bin:/bin",
           "RODEO_REPO_WAIT_TRIES": "5", "RODEO_REPO_WAIT_SECS": "1"}
    script = _function("wait_for_zypper_repos") + "wait_for_zypper_repos\n"
    r = subprocess.run(["bash", "-c", script], env=env, capture_output=True, text=True, timeout=30)
    return r, len(calls.read_text().splitlines())


def test_waits_until_cloud_registration_adds_a_repo(tmp_path):
    r, polls = _run(tmp_path, cloud=True, repos_after=3)
    assert r.returncode == 0
    assert polls == 3
    assert "Waiting for the cloud update server" in r.stdout


def test_no_wait_without_guestregister(tmp_path):
    r, polls = _run(tmp_path, cloud=False, repos_after=0)
    assert r.returncode == 0
    assert polls == 0
    assert r.stdout == ""


def test_gives_up_after_the_limit_and_lets_zypper_report(tmp_path):
    r, polls = _run(tmp_path, cloud=True, repos_after=0)
    assert r.returncode == 0
    assert polls == 5
    assert "installing anyway" in r.stderr


def test_prereq_install_calls_the_wait_before_zypper_install():
    text = INSTALL_SH.read_text()
    block = text[text.index('echo "==> Installing prerequisites"'):]
    assert block.index("wait_for_zypper_repos") < block.index("zypper --non-interactive install")
