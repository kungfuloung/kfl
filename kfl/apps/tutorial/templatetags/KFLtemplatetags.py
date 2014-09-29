# -*- coding: utf-8 -*-

from django import template
# from KPISetter.models import UserProfile
# from KPISetter.views import is_sub

from discussion.models import ThreadContent, Reply

register = template.Library()

@register.filter
def percentage(value):
	if value:
		return format(value, "2.0%")
	else:
		return ("0%")
# Create your tests here.

@register.filter
def level(value):

	temp = ''
	if value:
		if value>0:
			for i in range(value):
				temp = temp + '★'
	else:
		if value==0:
			temp = 'Not Ranked'
		else:
			temp = 'To Be Determined'

	return temp
	

@register.filter	
def tutsort(tutorials, value):
	# if tutorials:
	result = tutorials.filter(season=value).order_by('episode')
	return result



@register.filter	
def discreg(cat, value):
	# if tutorials:
	result = cat.filter(rid=value)
	return result



@register.filter	
def findcont(topic):
	# if tutorials:

	result = ThreadContent.objects.filter(of_thread=topic)
	return result





# replies of replies
@register.filter	
def r_of_r(reply):
	result = Reply.objects.filter(following_reply=reply).order_by('posted_on')
	return result



# @register.filter
# def has_sub(userprofile):
# 	result = False

# 	from django.db.models import Q				
# 	allWM = UserProfile.objects.filter(Q(job_function__name='Sales', user__is_active=True) | Q(job_function__name='Promoter', user__is_active=True)).order_by('-job_function','sales_unit')

# 	for member in allWM:
# 		if is_sub(member, userprofile):
# 			result = True
# 			break

# 	return result
		

# @register.filter
# def plus1(value):
# 	if value:
# 		return value+1
# 	else:
# 		return value
		

