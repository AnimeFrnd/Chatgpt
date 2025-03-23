import os
import logging
from logging.handlers import RotatingFileHandler


def get_int_env(var_name, default):
    try:
        return int(os.environ.get(var_name, default))
    except ValueError:
        return default  # Fallback to default if conversion fails


def str_to_bool(value):
    return str(value).lower() in ("true", "1", "yes")


BOT_TOKEN = os.environ.get("BOT_TOKEN", "5800464701:AAEcqurMoiZRO3vOGmgdvkqJg4NBOl3b0mQ")
API_ID = get_int_env("API_ID", 7515868)
API_HASH = os.environ.get("API_HASH", "dbd251e9ad4883b0443cc82b618ac6fa")

OWNER_ID = get_int_env("OWNER_ID", 6081617163)
DB_URL = os.environ.get("DB_URL", "mongodb+srv://bestanimeandcartoonsclips:VrMTuRFUEZdKsoV7@cluster0.ayqz3o3.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "aryabro")

CHANNEL_ID = get_int_env("CHANNEL_ID", -1002292066966)
FORCE_SUB_CHANNEL = get_int_env("FORCE_SUB_CHANNEL", -1001713521586)
FORCE_SUB_CHANNEL2 = get_int_env("FORCE_SUB_CHANNEL2", -1002129412433)
FORCE_SUB_CHANNEL3 = get_int_env("FORCE_SUB_CHANNEL3", -1001946212779)  # Added back
FORCE_SUB_CHANNEL4 = get_int_env("FORCE_SUB_CHANNEL4", -1002229481059)  # Added back

FILE_AUTO_DELETE = get_int_env("FILE_AUTO_DELETE", 86400)  # Auto delete in seconds
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = get_int_env("TG_BOT_WORKERS", 6)

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/703f6dd8194cb5d707d63-c4bfc450283f9a4b4b.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/703f6dd8194cb5d707d63-c4bfc450283f9a4b4b.jpg")

# Proper handling of admins
ADMINS = {6081617163}  # Use a set to avoid duplicates
env_admins = os.environ.get("ADMINS", "6081617163").split()
ADMINS.update(int(x) for x in env_admins if x.isdigit())  # Ensuring only valid numbers
ADMINS.add(OWNER_ID)  # Ensuring OWNER_ID is in ADMINS
ADMINS = list(ADMINS)  # Convert back to list for compatibility

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = str_to_bool(os.environ.get('PROTECT_CONTENT', "False"))
DISABLE_CHANNEL_BUTTON = str_to_bool(os.environ.get('DISABLE_CHANNEL_BUTTON', "True"))

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"

USER_REPLY_TEXT = "âŒsá´Ê€Ê€Ê à°®à°¾à°µà°¾ à°¨à±à°µà±à°µà± à°¨à°¾ á´á´¡É´á´‡Ê€ à°•à°¾à°¦à±..!ðŸ˜œ\n\nâŒDon't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = """<blockquote>
<b>Hey, <a href='tg://user?id={id}'>{first}</a>âœŒðŸ». I hope you're feeling the power of ð’Êœá´€á´…á´á´¡ Má´É´á´€Ê€á´„Êœ ðŸ˜ˆ.</b>

<b>I'm The Ultimate File Sharing Bot, built to rule the Shadow Realm ðŸ–¤</b>

ðŸ”± <b>Store & Share Files with a Single Click.</b>  
ðŸ›¡ï¸ <b>Infinite File Management System.</b>  
ðŸ“‚ <b>Post Files in Anime Monarch ðŸ‘‘ Template.</b>

---

<b>Now, The File Realm Is Under My Control ðŸ˜ˆ.</b>  
<b>Are You Ready to Dominate, {first}-Sama? ðŸ‘‘</b>
</blockquote>"""

FORCE_MSG = "Join my channels first ðŸ˜ˆ"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
