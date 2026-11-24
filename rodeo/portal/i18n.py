"""Student-facing strings: English is the source text and the catalog key.

``tr(lang, "English text")`` returns the translation for ``lang``, or the English
text itself when the language or the string has no translation, so a missing entry
never breaks a page. Catalog values are trusted HTML, like the English text they
replace. The instructor page stays in English.
"""

from __future__ import annotations

from typing import Any

from .claims import PIN_LENGTH

DEFAULT = "en"

# Taiwan usage; product and technical terms (lab, workshop, URL, SSH, PIN) stay in English.
ZH_TW = {
    "Hands-on labs": "實作 lab",
    "Hands-on lab": "實作 lab",
    "Privacy: we only keep your name and email for this workshop, deleted when it ends. "
    "Essential cookies only.": (
        "隱私權：我們只為這場 workshop 保存您的姓名與電子郵件，workshop 結束後即刪除。只使用必要的 cookie。"
    ),
    "Details": "詳細說明",
    "Open the workshop guide": "開啟 workshop 指南",
    "Workshop guide": "Workshop 指南",
    "Step-by-step exercises for this lab. Keep it open next to this page.": (
        "本 lab 的逐步練習，建議與本頁並排開啟。"
    ),
    "copy": "複製",
    "copied": "已複製",
    "{n} day": "{n} 天",
    "{n} days": "{n} 天",
    "{n} hour": "{n} 小時",
    "{n} hours": "{n} 小時",
    "{n} minute": "{n} 分鐘",
    "{n} minutes": "{n} 分鐘",
    "Protects the forms on this site from forged submissions.": "防止有人偽造本網站的表單送出。",
    "Until you close the browser": "直到您關閉瀏覽器",
    "Remembers that you entered the workshop code.": "記住您已輸入 workshop 代碼。",
    "Remembers this device so “Continue to your lab” can take you back. "
    "“Forget this device” removes it.": (
        "記住這台裝置，讓「前往您的 lab」帶您回到 lab。按「忘記這台裝置」即可移除。"
    ),
    "What we keep": "我們保存的資料",
    "<b>Your name and email</b>, to assign your lab and to give it back to you if you lose the page.": (
        "<b>您的姓名與電子郵件</b>：用來分配您的 lab，並在您找不到頁面時把 lab 找回給您。"
    ),
    "<b>Your PIN</b>, stored only as a one-way hash: nobody can read it, including the instructor.": (
        "<b>您的 PIN 碼</b>：只以單向雜湊值保存，任何人（包括講師）都無法讀取。"
    ),
    "<b>When you claimed and first opened your lab.</b>": "<b>您領取 lab 及第一次開啟 lab 的時間。</b>",
    "This is kept only on this workshop's own server. Your instructor can see which lab you "
    "have, with your name and email, to help you during the workshop, and can export that "
    "list (for example for attendance).": (
        "這些資料只保存在這場 workshop 自己的伺服器上。講師看得到您使用哪個 lab 以及您的姓名與電子郵件，"
        "以便在 workshop 期間協助您，也可以匯出這份名單（例如用於簽到）。"
    ),
    "How long": "保存多久",
    "Everything above is deleted when the workshop ends and this server is shut down.": (
        "workshop 結束、這台伺服器關閉時，以上資料全部刪除。"
    ),
    "What we do not do": "我們不做的事",
    "No tracking, analytics or advertising, and nothing is shared with third parties. "
    "Even the fonts and logo are served by this server.": (
        "不追蹤、不做分析、不放廣告，也不與第三方分享任何資料。連字型與 logo 都由這台伺服器提供。"
    ),
    "Your network address is not stored. To stop password guessing, the addresses of failed "
    "attempts are kept in memory for at most {window} and never written to disk.": (
        "不保存您的網路位址。為了防止有人猜測密碼，嘗試失敗的位址只會暫存在記憶體中最多 {window}，"
        "絕不寫入磁碟。"
    ),
    "Cookies": "Cookie",
    "Only these three, all needed for the portal to work. None of them tracks you.": (
        "只有以下三個，都是入口網站運作所必需，沒有一個會追蹤您。"
    ),
    "Name": "名稱",
    "Purpose": "用途",
    "Lasts": "保存期限",
    "Questions": "有問題嗎？",
    "Ask your instructor.": "請洽詢講師。",
    "Back to the portal": "回到入口網站",
    "Privacy": "隱私權",
    "Your data": "您的資料",
    "What this lab portal keeps, why, and for how long.": "這個 lab 入口網站保存哪些資料、原因，以及保存多久。",
    "Not you? Forget this device": "不是您嗎？忘記這台裝置",
    "Welcome back, {name}": "歡迎回來，{name}",
    "student": "學員",
    "This device remembers your lab <b>{lab}</b>.": "這台裝置記得您的 lab <b>{lab}</b>。",
    "Continue to your lab": "前往您的 lab",
    "Already have a lab? Get it back": "已經領取過 lab？在這裡找回",
    "Email": "電子郵件",
    "Your 6-digit PIN": "您的 6 位數 PIN 碼",
    "Locked out or forgot your PIN? Ask your instructor.": "被鎖住或忘記 PIN 碼？請洽詢講師。",
    "Get my lab back": "找回我的 lab",
    "Workshop code": "Workshop 代碼",
    "Continue": "繼續",
    "Enter the workshop code your instructor gives you.": "請輸入講師提供的 workshop 代碼。",
    "Open the personal link your instructor sent you to get your lab.": (
        "請開啟講師寄給您的個人連結，取得您的 lab。"
    ),
    "Claiming is closed. Ask your instructor.": "領取已關閉，請洽詢講師。",
    "Your name": "您的姓名",
    "6-digit PIN": "6 位數 PIN 碼",
    "Choose 6 digits that are not obvious (not 123456 or 111111). On another device, your "
    "email and this PIN get your lab back.": (
        "請選 6 個不容易被猜到的數字（不要用 123456 或 111111）。換到其他裝置時，"
        "用您的電子郵件和這組 PIN 碼就能找回 lab。"
    ),
    "Get my lab": "領取我的 lab",
    "Your name and email are used only to assign your lab and are deleted after the workshop.": (
        "您的姓名與電子郵件只用來分配 lab，workshop 結束後即刪除。"
    ),
    "Privacy details": "隱私權說明",
    "Claim your personal lab: it is yours for the whole workshop.": "領取您的個人 lab：整場 workshop 都歸您使用。",
    "User": "使用者",
    "Password": "密碼",
    "Host": "主機",
    "Port": "連接埠",
    "Download SSH key": "下載 SSH 金鑰",
    "Then, in the folder where you saved it:": "接著在存放金鑰的資料夾中執行：",
    "Labs": "Lab 列表",
    "{free} of {total} free": "尚有 {free} 個可領取，共 {total} 個",
    "State": "狀態",
    "Claimed by": "領取者",
    "free": "可領取",
    "claimed": "已領取",
    "building": "建置中",
    "Your lab": "您的 lab",
    "Personal link": "個人連結",
    "Assigned to {who}. Bookmark this page: it is your personal link. Do not share it.": (
        "已分配給 {who}。請把本頁加入書籤：這是您的個人連結，請勿分享。"
    ),
    "Still building": "建置中",
    "Your lab is not ready yet. This page refreshes every minute.": "您的 lab 尚未就緒，本頁每分鐘自動重新整理。",
    "SSH to your lab host": "SSH 連線到您的 lab 主機",
    "The lab web UIs use self-signed certificates. Accept the browser warning to continue.": (
        "lab 的網頁介面使用自簽憑證，請接受瀏覽器的警告後繼續。"
    ),
    "Slow down": "請稍候",
    "Too many attempts": "嘗試次數過多",
    "Wait a few minutes and try again.": "請等幾分鐘後再試一次。",
    "Too many wrong codes": "錯誤代碼過多",
    "Too many wrong workshop codes from your network. Wait a few minutes and try again, or "
    "ask your instructor.": (
        "您所在的網路送出太多錯誤的 workshop 代碼。請等幾分鐘後再試，或洽詢講師。"
    ),
    "Link not valid": "連結無效",
    "Claim a lab": "領取 lab",
    "This link was released or never existed.": "這個連結已被釋出或不存在。",
    "Not found": "找不到頁面",
    "Your session expired. Please submit again.": "您的工作階段已過期，請重新送出。",
    "That workshop code is not valid.": "這個 workshop 代碼無效。",
    # claims.ClaimError messages, shown to the student verbatim.
    "Enter a valid email.": "請輸入有效的電子郵件。",
    "Enter your name.": "請輸入您的姓名。",
    f"The PIN must be {PIN_LENGTH} digits.": f"PIN 碼必須是 {PIN_LENGTH} 位數字。",
    "That PIN is too easy to guess. Choose a less obvious one.": "這組 PIN 碼太容易被猜到，請換一組不明顯的數字。",
    "This workshop uses personal lab links. Use the one your instructor sent you.": (
        "這場 workshop 使用個人 lab 連結，請使用講師寄給您的連結。"
    ),
    "This email has a personal invite link. Use that link.": "這個電子郵件已有個人邀請連結，請使用該連結。",
    "This email already has a lab. Use “Get my lab back” below.": (
        "這個電子郵件已經領取過 lab，請使用下方的「找回我的 lab」。"
    ),
    "No free labs left. Ask your instructor.": "已經沒有可領取的 lab，請洽詢講師。",
    "No lab matches that email and PIN.": "找不到符合這組電子郵件與 PIN 碼的 lab。",
    "Too many wrong PINs for this email. Ask your instructor.": "這個電子郵件輸入錯誤 PIN 碼的次數過多，請洽詢講師。",
}

CATALOGS: dict[str, dict[str, str]] = {DEFAULT: {}, "zh-TW": ZH_TW}
LANGUAGES = tuple(CATALOGS)


def language(value: Any) -> str:
    """Supported language tag for ``value`` (case and ``_`` forgiven), else English."""
    want = str(value or "").strip().replace("_", "-").lower()
    return next((tag for tag in CATALOGS if tag.lower() == want), DEFAULT)


def tr(lang: str, text: str, **fields: Any) -> str:
    """``text`` in ``lang``, falling back to English; ``fields`` fill ``{name}`` slots."""
    out = CATALOGS.get(lang, {}).get(text, text)
    return out.format(**fields) if fields else out
