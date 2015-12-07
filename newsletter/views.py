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

def rawHtmlText(request):
    return render(request, 'rawHtmlText.html')

def reference(request):
	return render(request, "reference.html", {})


# View functions for programming languages
def html(request):
    return render(request, "HTML.html", {})

def css(request):
    return render(request, "css.html", {})

def js(request):
    return render(request, "js.html", {})

def bootstrap(request):
    return render(request, "bootstrap.html", {})

def perl(request):
    return render(request, "perl.html", {})

def php(request):
    return render(request, "php.html", {})

def nodejs(request):
    return render(request, "nodejs.html", {})

def python(request):
    return render(request, "python.html", {})

def django(request):
    return render(request, "django.html", {})

def ruby(request):
    return render(request, "ruby.html", {})

def db2(request):
    return render(request, "db2.html", {})

def mangodb(request):
    return render(request, "mangodb.html", {})

def postgresql(request):
    return render(request, "postgresql.html", {})

def mysql(request):
    return render(request, "mysql.html", {})

def sqlite(request):
    return render(request, "sqlite.html", {})

def hadoop(request):
    return render(request, "hadoop.html", {})