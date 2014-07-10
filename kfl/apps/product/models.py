# import datetime
# from django.db.models import Sum
# from django.db import models
# from django.contrib.auth.models import User, Group
# from django.core.validators import MaxValueValidator, MinValueValidator

# from AuthTool.models import *
# from AuthTool.models import UserProfile

import datetime
from django.db.models import Sum
from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import MaxValueValidator, MinValueValidator


from user_profiles.models import UserProfile

# from django.utils.image import Image

# from AuthTool.models import UserProfile
# from django.core.files.storage import FileSystemStorage
# fs = FileSystemStorage(location='/media/photos')
# 

    
# class UserProfile(models.Model):

#     # User.__unicode__ = user_new_unicode 
#     user = models.OneToOneField(User, unique=True)  
#     customer_number = models.CharField(max_length=30, null=True, blank=True)    
#     language = models.ForeignKey('Language')
#     purchased_product = models.ManyToManyField('DVDProduct', related_name='p_product', null=True, blank=True)
#     last_viewed_product = models.ManyToManyField('DVDProduct', related_name='v_product', null=True, blank=True)

#     translator_status = models.BooleanField(default=False)
#     master_status = models.BooleanField(default=False)
    

#     # line_manager = models.ForeignKey('self', related_name='l_manager', blank=True, null=True)


#     def __unicode__(self):
#         return self.user.username





class Language(models.Model):

    name = models.CharField(max_length=20)
    pid = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name




class DVDProduct(models.Model):

    # User.__unicode__ = user_new_unicode 
    # name = models.CharField(max_length=30, primary_key=True, blank=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    title_CN = models.CharField(max_length=30, blank=True, null=True)
    title_EN = models.CharField(max_length=30, blank=True, null=True)
    
    discription_CN = models.TextField(max_length=10000, blank=True, null=True)
    discription_EN = models.TextField(max_length=10000, blank=True, null=True)

    category = models.ForeignKey('ProductCategory', blank=True, null=True)
    language = models.ManyToManyField(Language, blank=True, null=True)

    youtube_link = models.URLField(blank=True, null=True)
    youku_link = models.URLField(blank=True, null=True)
    taobao_link = models.URLField(blank=True, null=True)
    
    paypal_button = models.URLField(blank=True, null=True)
    paypal_button_on_sale = models.URLField(blank=True, null=True)

    minute = models.IntegerField(blank=True, null=True)
    second = models.IntegerField(blank=True, null=True)

    DVD_quantity = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    price = models.FloatField(blank=True, null=True)
    price_on_sale = models.FloatField(blank=True, null=True)

    online_download = models.ManyToManyField('downloadProduct', blank=True, null=True)

    product_image = models.ImageField(upload_to='productimages', blank=True)

    # product_image = models.ImageField()
    
    
    # photo = models.ImageField(storage=fs)



    def __unicode__(self):
        return self.name

# class ProductImage(models.Model):
#   image_of = models.ForeignKey(DVDProduct, blank=True)
#   number = models.IntegerField(blank=True)
#   product_image = models.ImageField(blank=True)


class downloadProduct(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    section_no = models.IntegerField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    minute = models.IntegerField(blank=True, null=True)
    second = models.IntegerField(blank=True, null=True)

    price = models.FloatField(blank=True, null=True)

    # language = models.ForeignKey(Language, blank=True, null=True)

    def __unicode__(self):
        return self.name

class ProductCategory(models.Model):
    name_en = models.CharField(max_length=30, blank=True, null=True)
    name_cn = models.CharField(max_length=30, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name_en



class ProductBundle(models.Model):


    title_CN = models.CharField(max_length=30, blank=True, null=True)
    title_EN = models.CharField(max_length=30, blank=True, null=True)
    
    discription_CN = models.TextField(max_length=10000, blank=True, null=True)
    discription_EN = models.TextField(max_length=10000, blank=True, null=True)

    category = models.ManyToManyField(ProductCategory, blank=True, null=True)
    percent_off = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    products = models.ManyToManyField(DVDProduct, blank=True, null=True)

    product_image = models.ImageField(upload_to='productimages', blank=True)


    language = models.ManyToManyField(Language, blank=True, null=True)

    
    taobao_link = models.URLField(blank=True, null=True)    
    paypal_button = models.URLField(blank=True, null=True)
    paypal_button_on_sale = models.URLField(blank=True, null=True)


    def __unicode__(self):
        return self.title_EN



class ProductComment(models.Model):
    following_product = models.ForeignKey(DVDProduct, null=True, blank=True)
    following_comment = models.ForeignKey('self', null=True, blank=True)

    posted_by = models.ForeignKey(UserProfile, null=True, blank=True)
    posted_on = models.DateTimeField(null=True, blank=True)

    Content = models.TextField(max_length=10000, null=True, blank=True)
    
    def __unicode__(self):
        return self.id
