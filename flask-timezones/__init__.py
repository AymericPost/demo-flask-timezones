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

        if(tz in all_timezones):

            time = datetime.now( timezone(tz) )

            return time.strftime("%d/%m/%Y %H:%M:%S")
        else:
            return jsonify({"error": "BAD REQUEST", "message": "Fuseau horaire incorrect."}), 400
    

    return app