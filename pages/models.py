from django.db import models

# Create your models here.
class Pages(models.Model):                           # example of inheritance
    title = models.CharField(max_length=128)         # multiple examples of composits
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

