import datetime
from django.db import models


class CheckTime(models.Model):
    name          = models.CharField(max_length=50)
    time          = models.IntegerField(default=0)
    last_activity = models.DateTimeField(default=datetime.datetime.now())

    def to_dict(self):
        return {
            "time": self.time
        }

    def to_dict_answer(self):
        return {
            "name"         : self.name,
            "time"         : self.time,
            "last_activity": self.last_activity
        }


class CheckLocation(models.Model):
    name         = models.CharField(max_length=200, blank=True)
    longitude    = models.FloatField(default=0.0, blank=True)
    width        = models.FloatField(default=0.0, blank=True)
    width_window = models.FloatField(default=0.0, blank=True)
    country      = models.CharField(max_length=200, blank=True)
    city         = models.CharField(max_length=200, blank=True)
    region       = models.CharField(max_length=200, blank=True)
    timezone     = models.CharField(max_length=200, blank=True)
    create_at    = models.DateTimeField(default=datetime.datetime.now())

    def to_dict(self):
        return {
            "name"         : self.name,
            "longitude"    : self.longitude,
            "width"        : self.width,
            "width_window" : self.width_window,
            "country"      : self.country,
            "city"         : self.city,
            "region"       : self.region,
            "timezone"     : self.timezone,
            "create_at"     : self.create_at
        }
