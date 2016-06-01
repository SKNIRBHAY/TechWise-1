
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
    url(r'^hackathonEvents/$', 'newsletter.views.hackathonEvents',name='hackathonEvents'),
    url(r'^event/$','newsletter.views.event',name='event'),
    url(r'^watson_main/$', 'newsletter.views.watson_main',name='watson_main'),
    url(r'^analytics/$', 'newsletter.analytics.main', name='analytics'),
    url(r'^homepage/$', 'newsletter.views.homepage', name='homepage'),
    url(r'^reference/$', 'newsletter.views.reference', name='reference'),
    url(r'^stats/$', 'newsletter.views.stats', name='stats'),
    url(r'^rawHtmlText/$', 'newsletter.views.rawHtmlText', name='rawHtmlText'),
    url(r'^hStatic/$', 'newsletter.views.hStatic', name='hStatic'),
    url(r'^hStatic1/$', 'newsletter.views.hStatic1', name='hStatic1'),
    url(r'^workshops/$', 'newsletter.views.workshops', name='workshops'),
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