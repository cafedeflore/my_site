from django.db import models
from django.db import models
import datetime
import json

# Create your models here.

class Check_Task(models.Model):
    name = models.CharField(max_length=200, default="")
    sql_check = models.IntegerField(default=0)
    db_compare = models.IntegerField(default=0)
    config_check = models.IntegerField(default=0)
    pause_point_check = models.IntegerField(default=0)
    log_monitor = models.IntegerField(default=0)
    checklist = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'task'
    # create_time = models.TimeField()
    # create_time = models.DateTimeField(default="1980-01-01 00:00:00")
    def toJSON(self):
        fields = []
        print "laal"
        for field in self._meta.fields:
            fields.append(field.name)
        d = {}
        for attr in fields:
            d[attr] = getattr(self, attr)
        print d
        import json
        print json.dumps(d)
        return json.dumps(d)


