from django.db import models

# Create your models here.
class Byte(models.Model):
    text = models.CharField(max_length=30)

    def __str__(self):
        return self.text  
    