from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Feedbaack(models.Model):
    contact_name = models.CharField(max_length=30, blank=False)
    contact_email = models.EmailField(unique=True)
    content = models.CharField(blank=False, max_length=500)
    ip_add = models.CharField(max_length=120, default='ABC')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_email

    def get_absolute_url(self):
        return reverse('success')