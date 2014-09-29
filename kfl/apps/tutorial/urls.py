from django.conf.urls.defaults import *

urlpatterns = patterns('',
    
    
	url(r'^overview/$', 'tutorial.views.overview', name='tutorialoverview'),
    url(r'^(?P<tutorialname>[\w\-]+)/$', 'tutorial.views.tutorialview', name="tutorialdisplay"),     

)

