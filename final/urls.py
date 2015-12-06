"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^$', 'newsletter.views.index',name='index'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'final.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^watson/$', 'newsletter.views.watson',name='watson'),
    url(r'^event/$','newsletter.views.event',name='event'),
    url(r'^analytics/$', 'newsletter.analytics.main'),
    url(r'^watson_main/$', 'newsletter.views.watson_main',name='watson_main'),
    url(r'^analytics/$', 'newsletter.analytics.main', name='analytics'),
    url(r'^homepage/$', 'newsletter.views.homepage', name='homepage'),
    url(r'^stats/$', 'newsletter.views.stats', name='stats'),
    #url(r'^newsletter/', include('final.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)