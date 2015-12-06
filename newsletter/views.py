from django.shortcuts import render
from .forms import ContactForm, SignUpUser
from django.core.mail import send_mail
from django.contrib.auth.views import login
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    title = 'Sign Up'
    title = "Home Page of %s" %(request.user)
    form = SignUpUser(request.POST or None)
    context = {
        'title': title,
        'form': form
    }
    if form.is_valid():
        form.save()
        context = {
            'title':"Thank you"
        }
    return render(request, "index.html", context)

def contact(request):
    title = 'Hello, please leave us a message'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.iteritmes():
        #     print key, value
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')
       # print email, message, full_name

        subject = 'Site Contact Form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'brad.sangit@gmail.com']
        contact_message = "%s: %s via %s"%(form_full_name, form_message, form_email)
        send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
    context = {
        'form': form,
        'title': title,
    }
    return render(request, 'contactform.html', context)


def watson(request):
    title = 'hello man'
    context = {
        'title':title
    }

    return render(request,'watson.html', context)

def watson_main(request):
    title = 'hello'
    context = {
        'title': title
    }
    return render(request,'watson_main.html', context)

def homepage(request):
    if not request.user.is_authenticated():
        return login(request)
    else:
      return render(request, 'homepage.html')

def event(request):
    return render(request,'event.html')

def stats(request):
    return render(request, 'stats.html')