from django.db import models

# Create your models here.
class DealTask(models.Model):

    env = models.IntegerField(default=0)
    condition = models.TextField()
    proposer = models.CharField(max_length=100, default=None)
    system = models.CharField(max_length=100, default=None)
    details = models.CharField(max_length=1000, default=None)
    comment = models.CharField(max_length=1000, default=None)

    add_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(default=None)
    is_solved = models.IntegerField(default=0)
    is_valid = models.IntegerField(default=0)

    class Meta:
        db_table = 'deal_task'
        ordering = ('id',)
