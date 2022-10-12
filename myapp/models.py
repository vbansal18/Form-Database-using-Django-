from asyncio.windows_events import NULL
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(blank=False, null=False, max_length=122)
    email = models.CharField(max_length=122, blank=False, null=False)
    phone = models.CharField(max_length=12, blank=False, null=False)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name and self.email
    