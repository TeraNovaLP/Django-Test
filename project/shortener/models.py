from django.db import models

# Create your models here.


class URL(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.URLField(max_length=255)
