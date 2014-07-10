from django.conf.urls.defaults import *

urlpatterns = patterns('',
    
    
    
    url(r'^overview/$', 'product.views.overview', name="productoverview"),
    url(r'^(?P<productname>[\w\-]+)/$', 'product.views.productview', name="productdisplay"),     
    url(r'^category/(\d+)/$', 'product.views.productcategory', name="productcategory"),     
    url(r'^bundle/(\d+)/$', 'product.views.productbundleview', name="bundledisplay"),     
    
)

