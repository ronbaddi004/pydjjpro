from __future__ import unicode_literals
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.shortcuts import redirect, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from .forms import ContactForm
from .models import Feedbaack
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'pydjjapp/index.html', {})


def success(request):
    return render(request, 'pydjjapp/commentsucc.html', {})


def get_ip(request):
    try:
        x_forward = request.META.get("HTML_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip = ""
    return ip

def contact(request):
    print(request.META.get('REMOTE_ADDR'))
    form = ContactForm(request.POST or None)
    if form.is_valid():
        new_sub = form.save(commit=False)
        contact_name = form.cleaned_data['contact_name']
        contact_email = form.cleaned_data['contact_email']
        content = form.cleaned_data['content']
        new_old, created = Feedbaack.objects.get_or_create(contact_name=contact_name,contact_email=contact_email,content=content)
        if created:
            new_old.ip_add = get_ip(request)
            new_old.save()
            return HttpResponseRedirect(reverse('success'))
        
        # contact_name = request.POST.get('contact_name', '')
        # contact_email = request.POST.get('contact_email', '')
        # form_content = request.POST.get('content', '')
        # template = get_template('contact_temp.txt')

        # context = {
        #     'contact_name': contact_name,
        #     'contact_email': contact_email,
        #     'form_content': form_content,
        # }
        # content = template.render(context)

        # email = EmailMessage(
        #     "New contact form submission",
        #     content,
        #     "pydj" +'',
        #     ['ronbaddi004@gmail.com'],
        #     headers = {'Reply-To': contact_email }
        # )

        # email.send()
        # return redirect('contact')

    return render(request, 'pydjjapp/contactUs.html', {
        'form': form,
    })