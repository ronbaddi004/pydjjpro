from __future__ import unicode_literals
from .forms import ContactForm

from django.contrib import admin
from .models import Feedbaack
# Register your models here.

class FormAds( admin.ModelAdmin ):
    form = ContactForm
    # list_display = Feedbaack._meta.get_fields()


admin.site.register(Feedbaack, FormAds)