import os
import pyrogram

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config



if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "filter bot",
        bot_token=7537500061:AAFCoUzz03qi2h9w1LQCkM3dWGVI-yQ2n7c,
        api_id=25468417,
        api_hash=caa67b488c5c313c85847106b2d23d2f,
        plugins=plugins,
        workers=300
    )
    Config.AUTH_USERS.add(str(680815375))
    app.run()
