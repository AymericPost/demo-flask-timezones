from flask import Flask, jsonify
from pytz import all_timezones, timezone
from datetime import datetime

from models.TimezoneModel import TimezoneModel

def create_app():
    app = Flask(__name__)

    @app.route("/api/gmt/<gmt>")
    def get_gmt(gmt):
        tz = "Etc/GMT{}".format(
            (gmt.replace("-", "+"), gmt.replace("+", "-"))[gmt.startswith("+")]
        )

        return jsonify( TimezoneModel(tz).toJson() )
    

    return app