from flask import Flask, jsonify
from pytz import all_timezones, timezone
from datetime import datetime

def create_app():
    app = Flask(__name__)

    @app.route("/api/gmt/<gmt>")
    def get_gmt(gmt):
        tz = "Etc/GMT{}".format(
            (gmt.replace("-", "+"), gmt.replace("+", "-"))[gmt.startswith("+")]
        )

        tzForGmt = []

        if(tz in all_timezones):
            current = datetime.now( timezone(tz) ).strftime("%d/%m/%Y %H:%M:%S")

            for one_timezone in all_timezones:
                time = datetime.now( timezone(one_timezone) ).strftime("%d/%m/%Y %H:%M:%S")

                if("Etc" not in one_timezone and "/" in one_timezone and current == time):
                    tzForGmt.append(one_timezone)

            return jsonify({"timezone": "GMT{}".format(gmt),"time": current, "locales": tzForGmt})
        else:
            return jsonify({"error": "BAD REQUEST", "message": "Fuseau horaire incorrect."}), 400
    

    return app