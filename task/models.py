from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Message(models.Model):
    message = models.CharField(max_length=30,verbose_name="message")

    def __str__(self):
        return self.message

