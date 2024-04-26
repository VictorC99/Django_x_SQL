from django.db import models

class Task(models.Model):
    title = models.CharField(max_length = 200)
def _str_ (self):
    return self.title