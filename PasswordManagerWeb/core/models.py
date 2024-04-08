from django.db import models
from django.urls import reverse


# Create your models here.
class Site(models.Model):
    website_name = models.CharField(max_length=50)
    website_link = models.URLField(max_length=200, null=True)
    website_username = models.CharField(max_length=50)
    website_password = models.CharField(max_length=50)
    website_notes = models.CharField(max_length=50, null=True)
    master_password = models.CharField(max_length=200, default='')

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website_name

    def get_absolute_url(self):
        return reverse("home")
