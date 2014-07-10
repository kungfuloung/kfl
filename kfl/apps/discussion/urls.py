from django.conf.urls.defaults import *

urlpatterns = patterns('',
    
    
    url(r'^overview/$', 'discussion.views.overview'),
    url(r'^category/(\d+)/$', 'discussion.views.threadcategory', name="threadcategory"),     
    url(r'^searchresults/$', 'discussion.views.threadresult'),     
    url(r'^searchresults/(?P<posted_by>[\w\-]+)/$', 'discussion.views.threadresultpostedby', name="threadpostedby"),     
    url(r'^searchresults/inlanguage/(?P<inlanguage>[\w\-]+)/$', 'discussion.views.threadresultinlanguage', name="threadinlanguage"),     

    url(r'^post/(\d+)/$', 'discussion.views.threadpost', name="postcategory"),     
    url(r'^thread/(\d+)/$', 'discussion.views.threaddetail', name="threaddetail"),     
    url(r'^topic/(\d+)/language/(\d+)/$', 'discussion.views.topiclanguagesearch', name="topiclanguagesearch"),     

    url(r'^thread/(\d+)/(\d+)/reply/$', 'discussion.views.postreply', name="postreply"),     
    url(r'^post/reply/(\d+)/(\d+)/$', 'discussion.views.replyreply', name="replyreply"),     
    url(r'^topic/(\d+)/thread/(\d+)/translate/$', 'discussion.views.threadtranslate', name="threadtranslate"),     
    url(r'^topic/(\d+)/delete/$', 'discussion.views.threaddelete', name="threaddelete"),     

    url(r'^thread/(\d+)/masterreply/$', 'discussion.views.masterreply', name="masterreply"),     
    
)

