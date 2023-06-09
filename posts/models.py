from django.db import models
from django.urls import reverse
# create models

class Post(models.Model):                           # example of inheritance
    title = models.CharField(max_length=128)         # multiple examples of composits
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])


