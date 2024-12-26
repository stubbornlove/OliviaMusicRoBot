from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("29376235"))
API_HASH = getenv("d7c10b0e14c1355dde0fec9d37c19b54")
BOT_TOKEN = getenv("7686693076:AAHNYZfoP0JdDnS8Ldy3XhLo1_uEjzmkuKc")
OWNER_ID = int(getenv("6517946837"))

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/84819fc115cb0eff32b2b.jpg")

SESSION = getenv("AQHAPusAvOzyjgZmb1wcXF0Y8-lpsyTVc88S_liAzLgzCkwkHRESOOi6ku8PmzWiJADbE4ZjSntYpdvbl1TLjIgmoyzRfSF42dHxJUuQTS9R3dDEtIOY9XH7qQWjDAl4qIrFT-O7bNVleqbu9xyQRqJRdgBFrMRJgA-SCYS0H17NO0-OfAHIjcErmNvLgW-VpUVCofLHSJgJkHGJHZpvXFo0dpKdH_Tz0QSG3OuylIuSSDxUp6O-wrcTfHPv2fP8_JOFFCP_WMHfk9ev1OOVZ1RKOjK2IE0VdjsyFp18yX0sI4goPg3zNeQOhlkHqxtXyDq8xGG-zfqEDuQjsJROcUceB2S31QAAAAGEf_nVAA")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tbcbotschat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tbc_bots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7353883554").split()))
FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
