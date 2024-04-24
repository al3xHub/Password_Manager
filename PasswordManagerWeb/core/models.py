from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Site(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website_name = models.CharField(max_length=50)
    website_link = models.CharField(max_length=200, null=True, blank=True)
    website_username = models.CharField(max_length=50)
    website_password = models.CharField(max_length=50)
    website_notes = models.CharField(max_length=200, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website_name

    def get_absolute_url(self):
        return reverse("home")
