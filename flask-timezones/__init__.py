from flask import Flask
from pytz import all_timezones, timezone
from datetime import datetime

def create_app():
    app = Flask(__name__)

    @app.route("/api/gmt/<gmt>")
    def get_gmt(gmt):
        time = datetime.now( timezone("Etc/GMT{}".format(gmt)) )

        return time.strftime("%d/%m/%Y %H:%M:%S")
    

    return app