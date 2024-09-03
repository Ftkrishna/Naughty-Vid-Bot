

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "24440741"))
	API_HASH = os.environ.get("API_HASH", "eda231ff278ef43dc36164de83ee8fd6")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	UR_CHANNEL = os.environ.get("UR_CHANNEL", "-1002238297424") 
	UR_GROUP = os.environ.get("UR_GROUP", "-1002159673469")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "NaughtyX11")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002240732384"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "6307223516"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://megadiwani:gnTnDjCx1jB9W9hg@cluster0.ak69r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002185599613"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	HOME_TEXT = os.environ.get("HOME_TEXT")
