from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'globals.views.home', name="globals-home"),
    url(r'^$', 'product.views.homepage'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^logout/$', 'globals.views.globals_logout', name="globals-logout"),

    (r'^api/', include('api.urls')),
    (r'^discussion/', include('discussion.urls')),
    (r'^products/', include('product.urls')),
    (r'^tutorials/', include('tutorial.urls')),

    url(r'^set_cn/$', 'product.views.set_cn'),
    url(r'^set_en/$', 'product.views.set_en'),

)

urlpatterns += staticfiles_urlpatterns()
