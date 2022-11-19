# (c) @Roiderff
import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 23030151))
    API_HASH = os.environ.get("API_HASH", "3853c9cfaa64c9eae9dfead46c0dac63")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5891645935:AAG37uqchOj5NwfFRSo6q_mlg4xRAQ1zo38")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "allnew_movie<request_bot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "1BVtsOIsBu2LW4Pinq4AUOVaUdVXRLyg5yswHkglJ5wltykYPmXKD3UtWBTO4nfpeuGP4uhP5w_BT-z5kBK7fZ5oad2xKCyd_uotEAWydt6xPIPaFqZqtI4JsiiJ35Kz61n61Nz-Rrz9-X6j1MvuxOhXMBRvC2dCUtVfVT1TAN0R09Y4Qn2JCTHexeS4ieVZWtzY7ZfFGKIM679qLaP6PR36SBAaB-nZFjeVGC3JVRExBnIfCwSmU2LRsJP7-4IUM9BsmSFQlSFnJ5C_gjvuStoyhqbdt-njx2UQ2XfrkWr9GglJYppiLdIGbuxACvcsjscOfJJWx_AESa0FVN5U42q7I-n0J150=")
    CHANNEL_ID = int(os.environ.get("-1001828630319", -100))
    BOT_USERNAME = os.environ.get("allnew_movie<request_bot")
    BOT_OWNER = int(os.environ.get("@Roiderff"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/mdisk_all_new_movies_bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/cyniteofficial'>Click Me</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @Cyniteofficial</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @roiderff</a></b>
"""


