from django.db import models

# Create your models here.


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    