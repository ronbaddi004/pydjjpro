from django import forms
from .models import Feedbaack
# our new form

class ContactForm(forms.ModelForm):
    content = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Feedbaack
        fields = '__all__'
        # fields = ["contact_name", "contact_email", "content",]
        # exclude = ['ip_add']s