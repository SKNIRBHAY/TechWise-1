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
    url(r'^watson_main/$', 'newsletter.views.watson_main',name='watson_main'),
    url(r'^analytics/$', 'newsletter.analytics.main', name='analytics'),
    url(r'^homepage/$', 'newsletter.views.homepage', name='homepage'),
    url(r'^reference/$', 'newsletter.views.reference', name='reference'),
    url(r'^stats/$', 'newsletter.views.stats', name='stats'),
    url(r'^rawHtmlText/$', 'newsletter.views.rawHtmlText', name='rawHtmlText'),
    #url(r'^newsletter/', include('final.urls'))

    #Language Pages
    url(r'^reference/html/$', 'newsletter.views.html', name='html'),
    url(r'^reference/css/$', 'newsletter.views.css', name='css'),
    url(r'^reference/js/$', 'newsletter.views.js', name='js'),
    url(r'^reference/bootstrap/$', 'newsletter.views.bootstrap', name='bootstrap'),
    url(r'^reference/perl/$', 'newsletter.views.perl', name='perl'),
    url(r'^reference/php/$', 'newsletter.views.php', name='php'),
    url(r'^reference/nodejs/$', 'newsletter.views.nodejs', name='nodejs'),
    url(r'^reference/python/$', 'newsletter.views.python', name='python'),
    url(r'^reference/django/$', 'newsletter.views.django', name='django'),
    url(r'^reference/ruby/$', 'newsletter.views.ruby', name='ruby'),
    url(r'^reference/db2/$', 'newsletter.views.db2', name='db2'),
    url(r'^reference/mangodb/$', 'newsletter.views.mangodb', name='mangodb'),
    url(r'^reference/postgresql/$', 'newsletter.views.postgresql', name='postgresql'),
    url(r'^reference/mysql/$', 'newsletter.views.mysql', name='mysql'),
    url(r'^reference/sqlite/$', 'newsletter.views.sqlite', name='sqlite'),
    url(r'^reference/hadoop/$', 'newsletter.views.hadoop', name='hadoop')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)