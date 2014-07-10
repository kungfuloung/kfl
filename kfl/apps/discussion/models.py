import datetime
from django.db.models import Sum
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from product.models import UserProfile, Language


class ThreadCategory(models.Model):

    rid = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)

    title_CN = models.CharField(max_length=30, blank=True, null=True)
    title_EN = models.CharField(max_length=30, blank=True, null=True)
    
    discription_CN = models.TextField(max_length=10000, blank=True, null=True)
    discription_EN = models.TextField(max_length=10000, blank=True, null=True)

    def __unicode__(self):
        return self.title_CN

class Thread(models.Model):

    category = models.ForeignKey(ThreadCategory, blank=True, null=True)

    youtube_link = models.URLField(blank=True, null=True)
    youku_link = models.URLField(blank=True, null=True)

    # update_time = models.DateTimeField(null=True, blank=True)
    update_on = models.DateTimeField(null=True, blank=True)
    update_by = models.ForeignKey(UserProfile, null=True, blank=True)

    reply_number = models.IntegerField(default=0)
    def __unicode__(self):
        return str(self.id)



class ThreadContent(models.Model):
    title = models.CharField(max_length=400, null=True, blank=True)

    Content = models.TextField(max_length=10000, null=True, blank=True) 

    language = models.ForeignKey(Language, null=True, blank=True)

    posted_by = models.ForeignKey(UserProfile, related_name='p_by', null=True, blank=True)
    posted_on = models.DateTimeField(null=True, blank=True)
    
    replied_by_master = models.BooleanField(default=False)


    master_content = models.TextField(max_length=10000, null=True, blank=True)  
    replied_by = models.ForeignKey(UserProfile, related_name='r_by', null=True, blank=True)
    replied_on = models.DateTimeField(null=True, blank=True)    
    
    # translated_thread = models.ManyToManyField('self', related_name='t_thread', null=True, blank=True)
    of_thread = models.ForeignKey(Thread, blank=True)
    related_thread = models.ManyToManyField('self', related_name='r_thread', null=True, blank=True)


    # name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.title





class Reply(models.Model):
    following_thread = models.ForeignKey(Thread, null=True, blank=True)
    following_reply = models.ForeignKey('self', null=True, blank=True)

    Content = models.TextField(max_length=10000, null=True, blank=True)

    posted_by = models.ForeignKey(UserProfile, null=True, blank=True)
    posted_on = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return str(self.id)
    
    

# class ForumCategory(models.Model):
#   name = 