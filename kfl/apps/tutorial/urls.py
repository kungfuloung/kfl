from django.conf.urls.defaults import *

urlpatterns = patterns('',
    
    
    
	url(r'^overview/$', Tutorial.views.overview),
    url(r'^(?P<tutorialname>[\w\-]+)/$', Tutorial.views.tutorialview, name="tutorialdisplay"),     

)

