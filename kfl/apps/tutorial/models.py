from django.db import models
from KFLProduct.models import UserProfile



# Create your models here.




class VideoTutorial(models.Model):


    category = models.ForeignKey('TutorialCategory', null=True, blank=True)

    season = models.IntegerField(null=True, blank=True)
    episode = models.IntegerField(null=True, blank=True)
    
    youtube_link = models.URLField(blank=True, null=True)
    youku_link = models.URLField(blank=True, null=True)

    minute = models.IntegerField(blank=True, null=True)
    second = models.IntegerField(blank=True, null=True)


    def __unicode__(self):
        return self.category.name


class TutorialCategory(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    tutorial_pic = models.ImageField(upload_to='tutorialimages', blank=True)

    title_CN = models.CharField(max_length=30, blank=True, null=True)
    title_EN = models.CharField(max_length=30, blank=True, null=True)   

    discription_CN = models.TextField(max_length=10000, blank=True, null=True)
    discription_EN = models.TextField(max_length=10000, blank=True, null=True)


    def __unicode__(self):
        return self.name


class TutorialComment(models.Model):
    following_tutorial = models.ForeignKey(VideoTutorial, null=True, blank=True)
    following_comment = models.ForeignKey('self', null=True, blank=True)

    posted_by = models.ForeignKey(UserProfile, null=True, blank=True)
    posted_on = models.DateTimeField(null=True, blank=True)

    Content = models.TextField(max_length=10000, null=True, blank=True)
    