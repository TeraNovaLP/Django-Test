from django.db import models


# Create your models here.
class ToDo(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
