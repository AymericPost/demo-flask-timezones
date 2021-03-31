from pytz import all_timezones, timezone
from datetime import datetime

class TimezoneModel():
    tz = str()
    time = str()
    locales = list()

    hour = {
        "hour": int(),
        "minute": int(),
        "second": int()
    }

    date = {
        "day": int(),
        "month": int(),
        "year": int()
    }

    def __init__(self, tz):
        if(tz in all_timezones):
            self.tz = tz
        else:
            raise ValueError("Timezone '{}' doesn't exists.".format(tz))
        
        now = datetime.now( timezone(tz) )
        
        self.time = now.strftime("%d/%m/%Y %H:%M:%S")

        self.hour["hour"] = int( now.strftime("%H") )
        self.hour["minute"] = int( now.strftime("%M") )
        self.hour["second"] = int( now.strftime("%S") )

        self.date["day"] = int( now.strftime("%d") )
        self.date["month"] = int( now.strftime("%m") )
        self.date["year"] = int( now.strftime("%Y") )

        for one_timezone in all_timezones:
            timeForChecking = datetime.now( timezone(one_timezone) ).strftime("%d/%m/%Y %H:%M:%S")

            if("Etc" not in one_timezone and "/" in one_timezone and self.time == timeForChecking):
                    self.locales.append(one_timezone)
    
    def toJson(self):
        return {
            "timezone": self.tz,
            "time": self.time,
            "hour": self.hour,
            "date": self.date,
            "locales": self.locales
        }

