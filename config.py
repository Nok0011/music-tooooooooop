from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", '8186557'))
        self.API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")

        self.BOT_TOKEN = getenv("BOT_TOKEN")
        self.BOT_USERNAME = getenv("BOT_USERNAME") 
        self.BOT_ID = getenv("BOT_ID") 
        self.BOT_NAME = getenv("BOT_NAME")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://kuldiprathod2003:kuldiprathod2003@cluster0.wxqpikp.mongodb.net/?retryWrites=true&w=majority")

        owner_id_str = getenv("OWNER_ID", "8368077406")
        self.OWNER_ID = int(owner_id_str)
        self.LOGGER_ID = self.OWNER_ID 
        self.OWNER_USERNAME = getenv("OWNER_USERNAME")

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 90)) * 90
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", None)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/vegaone")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Cybervega")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
    
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://qu.ax/AUKFy.jpg")
        self.GITHUB_REPO_URL = "https://raw.githubusercontent.com/TOPVEGA/Ber/main/"
        self.GITHUB_FILES = ["Ninja.py"]
        self.ONE_VIDEO_URL = "https://files.catbox.moe/qkj2yd.mp4"
        self.PING_IMG = getenv("PING_IMG", "https://qu.ax/aTong.jpg")
        self.START_IMG = getenv("START_IMG", "https://qu.ax/aTong.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")


