import datetime
from django.db import models


class CheckTime(models.Model):
    name = models.CharField(max_length=50)
    time = models.IntegerField(default=0)
    last_activity = models.DateTimeField(default=datetime.datetime.now())

    def to_dict(self):
        return {
            "time": self.time
        }

    def to_dict_answer(self):
        return {
            "name": self.name,
            "time": self.time,
            "last_activity": self.last_activity
        }

# Create your models here.
