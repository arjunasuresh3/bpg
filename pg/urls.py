from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('bpg.views',
    url(r'^bpg/$', 'index'),
    url(r'^bpg/(?P<area_id>\d+)/$', 'detail'),
)

urlpatterns += patterns('',
    # url(r'^$', 'pg.views.home', name='home'),
    # url(r'^pg/', include('pg.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATICFILES_DIRS}),
)
