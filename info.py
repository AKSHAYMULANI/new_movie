import re
from os import environ
from Script import script

# Allow negative ids (e.g. -1001234567890 for channels) and normal integers
id_pattern = re.compile(r"^-?\d+$")


def is_enabled(value, default):
    """
    Accepts boolean, or a string value (from environ).
    Returns boolean.
    """
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    v = str(value).strip().lower()
    if v in ("true", "yes", "1", "enable", "y"):
        return True
    if v in ("false", "no", "0", "disable", "n"):
        return False
    return default


def parse_id(value):
    """
    Return int if value is a valid numeric id, else None.
    """
    if value is None:
        return None
    s = str(value).strip()
    if id_pattern.fullmatch(s):
        try:
            return int(s)
        except ValueError:
            return None
    return None


def parse_list_of_ids(env_value, default_list):
    """
    Parse a whitespace-separated env var into ints when numeric, else keep string tokens.
    Example: "933064491 -1001234567890 username"
    """
    raw = environ.get(env_value)
    if raw is None:
        raw = " ".join(default_list) if default_list else ""
    items = [tok.strip() for tok in raw.split() if tok.strip()]
    parsed = []
    for tok in items:
        if id_pattern.fullmatch(tok):
            try:
                parsed.append(int(tok))
            except ValueError:
                parsed.append(tok)
        else:
            parsed.append(tok)
    return parsed


# Main
SESSION = environ.get("SESSION", "Media_search")
API_ID = int(environ.get("API_ID", "35374854"))
API_HASH = environ.get("API_HASH", "d76d93afbf6eb569ba6fe2ad3e6f0d1e")
BOT_TOKEN = environ.get("BOT_TOKEN", "8392806853:AAG5nrcRnSRmX5PDohWK9E0t4uRGvDC2Bt4")
PORT = environ.get("PORT", "8082")

# Owners
ADMINS = parse_list_of_ids("ADMINS", ["933064491"])
OWNER_USERNAME = environ.get("OWNER_USERNAME", "akshaymulani")  # without @
USERNAME = environ.get("USERNAME", "akshaymulani")  # ADMIN USERNAME

# Database Channel(s)
# Provide a sane default or make it empty list if you don't want one
CHANNELS = parse_list_of_ids("CHANNELS", ["-1003291791362"])

# ForceSub Channel & Log Channels
AUTH_CHANNEL = parse_id(environ.get("AUTH_CHANNEL", "-1003291791362"))
AUTH_REQ_CHANNEL = parse_id(environ.get("AUTH_REQ_CHANNEL", "-1003291791362"))

# For optional channels, DO NOT default to 0 (0 is invalid peer). Use None if not set.
LOG_CHANNEL = parse_id(environ.get("LOG_CHANNEL", None))
LOG_API_CHANNEL = parse_id(environ.get("LOG_API_CHANNEL", None))
LOG_VR_CHANNEL = parse_id(environ.get("LOG_VR_CHANNEL", None))

# MongoDB
DATABASE_URI = environ.get(
    "DATABASE_URI",
    "mongodb+srv://marutee:marutee@marutee.ekweprt.mongodb.net/?appName=marutee",
).strip()
DATABASE_NAME = environ.get("DATABASE_NAME", "marutee").strip()

# Files index database url: prefer FILES_DATABASE env var; fallback to DATABASE_URI
FILES_DATABASE = environ.get("FILES_DATABASE", "").strip() or DATABASE_URI
# Basic validation — avoid empty string that caused ConfigurationError
if not FILES_DATABASE or "mongodb" not in FILES_DATABASE:
    raise RuntimeError(
        "FILES_DATABASE is missing or invalid. Set FILES_DATABASE or DATABASE_URI env var to a valid MongoDB URI."
)

COLLECTION_NAME = environ.get("COLLECTION_NAME", "jisshu")

# Other Channel's
SUPPORT_GROUP = parse_id(environ.get("SUPPORT_GROUP", None))
DELETE_CHANNELS = parse_id(environ.get("DELETE_CHANNELS", None))

request_channel = environ.get("REQUEST_CHANNEL", None)
REQUEST_CHANNEL = parse_id(request_channel)

MOVIE_UPDATE_CHANNEL = parse_id(environ.get("MOVIE_UPDATE_CHANNEL", None))

# Added Link Here Not Id
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "https://t.me/akshaymulani")
MOVIE_GROUP_LINK = environ.get(
    "MOVIE_GROUP_LINK", "https://t.me/+U9oTBETpkpg4YzNl"
)

# Verification
IS_VERIFY = is_enabled(environ.get("IS_VERIFY", None), True)

TUTORIAL = environ.get("TUTORIAL", "https://t.me/")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/")
VERIFY_IMG = environ.get(
    "VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg"
)
SHORTENER_API = environ.get("SHORTENER_API", "1bb101f6edcd5e1298f96b50a78f15252a3f8f4d")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "arolinks.com")
SHORTENER_API2 = environ.get("SHORTENER_API2", SHORTENER_API)
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", SHORTENER_WEBSITE)
SHORTENER_API3 = environ.get("SHORTENER_API3", SHORTENER_API)
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", SHORTENER_WEBSITE)
TWO_VERIFY_GAP = int(environ.get("TWO_VERIFY_GAP", "14400"))
THREE_VERIFY_GAP = int(environ.get("THREE_VERIFY_GAP", "14400"))

# Language & Quality & Season & Year
LANGUAGES = [
    "hindi",
    "english",
    "telugu",
    "tamil",
    "kannada",
    "malayalam",
    "bengali",
    "marathi",
    "gujarati",
    "punjabi",
    "marathi",
]
QUALITIES = [
    "HdRip",
    "web-dl",
    "bluray",
    "hdr",
    "fhd",
    "240p",
    "360p",
    "480p",
    "540p",
    "720p",
    "960p",
    "1080p",
    "1440p",
    "2K",
    "2160p",
    "4k",
    "5K",
    "8K",
]
YEARS = [f"{i}" for i in range(2025, 2002, -1)]
SEASONS = [f"season {i}" for i in range(1, 23)]

# Pictures And Reaction
START_IMG = (
    environ.get(
        "START_IMG",
        "https://i.ibb.co/qpxpGmC/image.jpg https://i.ibb.co/DQ35zLZ/image.jpg",
    )
).split()
FORCESUB_IMG = environ.get("FORCESUB_IMG", "https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg")
REFER_PICS = (environ.get("REFER_PICS", "https://envs.sh/PSI.jpg")).split()
PAYPICS = (
    environ.get("PAYPICS", "https://graph.org/file/f4db1c3ad3d9e38b328e6.jpg")
).split()
SUBSCRIPTION = environ.get(
    "SUBSCRIPTION", "https://graph.org/file/9f3f47c690bbcc67633c2.jpg"
)
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]

# Other Functions
FILE_AUTO_DEL_TIMER = int(environ.get("FILE_AUTO_DEL_TIMER", "600"))
AUTO_FILTER = is_enabled(environ.get("AUTO_FILTER", None), True)
IS_PM_SEARCH = is_enabled(environ.get("IS_PM_SEARCH", None), False)
IS_SEND_MOVIE_UPDATE = is_enabled(environ.get("IS_SEND_MOVIE_UPDATE", None), False)
MAX_BTN = int(environ.get("MAX_BTN", "8"))
AUTO_DELETE = is_enabled(environ.get("AUTO_DELETE", None), True)
DELETE_TIME = int(environ.get("DELETE_TIME", "1200"))
IMDB = is_enabled(environ.get("IMDB", None), False)
FILE_CAPTION = environ.get("FILE_CAPTION", f"{script.FILE_CAPTION}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", None), False)
PROTECT_CONTENT = is_enabled(environ.get("PROTECT_CONTENT", None), False)
SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK", None), True)
LINK_MODE = is_enabled(environ.get("LINK_MODE", None), True)
TMDB_API_KEY = environ.get("TMDB_API_KEY", "")

# Online Streaming And Download
STREAM_MODE = is_enabled(environ.get("STREAM_MODE", None), True)

MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes

ON_HEROKU = bool(environ.get("DYNO", False))
URL = environ.get("FQDN", "")

# Commands
admin_cmds = [
    "/add_premium - Add A User To Premium",
    "/premium_users - View All Premium Users",
    "/remove_premium - Remove A User's Premium Status",
    "/add_redeem - Generate A Redeem Code",
    "/refresh - Refresh Free Trial",
    "/set_muc - Set Movie Update Channel",
    "/pm_search_on - Enable PM Search",
    "/pm_search_off - Disable PM Search",
    "/set_ads - Set Advertisements",
    "/del_ads - Delete Advertisements",
    "/setlist - Set Top Trending List",
    "/clearlist - Clear Top Trending List",
    "/verify_id - Verification Off ID",
    "/index - Index Files",
    "/send - Send Message To A User",
    "/leave - Leave A Group Or Channel",
    "/ban - Ban A User",
    "/unban - Unban A User",
    "/broadcast - Broadcast Message",
    "/grp_broadcast - Broadcast Messages To Groups",
    "/delreq - Delete Join Request",
    "/channel - List Of Database Channels",
    "/del_file - Delete A Specific File",
    "/delete - Delete A File(By Reply)",
    "/deletefiles - Delete Multiple Files",
    "/deleteall - Delete All Files",
]

cmds = [
    {"start": "Start The Bot"},
    {"most": "Get Most Searches Button List"},
    {"trend": "Get Top Trending Button List"},
    {"mostlist": "Show Most Searches List"},
    {"trendlist": "𝖦𝖾𝗍 𝖳𝗈𝗉 𝖳𝗋𝖾𝗇𝖽𝗂𝗇𝗀 𝖡𝗎𝗍𝗍𝗈𝗇 𝖫𝗂𝗌t"},
    {"plan": "Check Available Premium Membership Plans"},
    {"myplan": "Check Your Currunt Plan"},
    {"refer": "To Refer Your Friend And Get Premium"},
    {"stats": "Check My Database"},
    {"id": "Get Telegram Id"},
    {"font": "To Generate Cool Fonts"},
    {"details": "Check Group Details"},
    {"settings": "Change Bot Setting"},
    {"grp_cmds": "Check Group Commands"},
    {"admin_cmds": "Bot Admin Commands"},
]
