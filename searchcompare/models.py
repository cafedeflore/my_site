from django.db import models

# Create your models here.
class CommentRecord(models.Model):
    keyword = models.CharField(max_length=100)
    choice = models.IntegerField()
    comments = models.CharField(max_length=2000, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

