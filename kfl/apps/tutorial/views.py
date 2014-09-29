from django.template.loader import get_template
from django.shortcuts import render
from django.contrib import auth
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required  

import datetime

from KFLProduct.models import UserProfile
from KFLProduct.views import setlanguage

from Tutorial.models import TutorialCategory, VideoTutorial

# Create your views here.

from django.views.decorators.csrf import csrf_protect


# Create your views here.




def overview(request):

    lan = setlanguage(request)
    state = ''

    user = request.user
    username = user.username

    displayed_tutorials = TutorialCategory.objects.all()

    return render_to_response('tutorial_overview.html',{'displayed_tutorials':displayed_tutorials, 'state':state, 'username':username, 'user':user, 'lan':lan}, RequestContext(request))

def tutorialview(request, tutorialname):

    lan = setlanguage(request)
    state = ''

    user = request.user
    username = user.username

    tutorialcat = TutorialCategory.objects.get(name=tutorialname)

    alltutorials = VideoTutorial.objects.filter(category=tutorialcat).order_by('episode').order_by('season')


    return render_to_response('tutorial_detailview.html',{'alltutorials':alltutorials, 'tutorialcat':tutorialcat, 'state':state, 'username':username, 'user':user, 'lan':lan}, RequestContext(request))


