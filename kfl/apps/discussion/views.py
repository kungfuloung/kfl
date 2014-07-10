# -*- coding: utf-8 -*-

from django.template.loader import get_template
from django.shortcuts import render
from django.contrib import auth
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required  

import datetime

from product.models import UserProfile, Language
from product.views import setlanguage

from discussion.models import Thread, Reply, ThreadCategory, ThreadContent
from discussion.forms import ForumSearchForm_cn, ForumSearchForm_en, ThreadPostForm, ReplyPostForm
# Create your views here.

from django.views.decorators.csrf import csrf_protect



# Create your views here.



# @login_required
def overview(request):

    lan = setlanguage(request)


    state = ''
    user = request.user
    username = user.username

    allcategory = ThreadCategory.objects.all().order_by('pid')


    if lan == 'en':
        form = ForumSearchForm_en
    if lan == 'cn':
        form = ForumSearchForm_cn            





    return render_to_response('discussion_overview.html',{'form':form, 
                                                          'allcategory':allcategory, 
                                                          'state':state, 
                                                          'username':username, 'user':user, 'lan':lan}, RequestContext(request))



def threadresult(request):

    lan = setlanguage(request)


    state = []
    user = request.user
    username = user.username
    if username:
        userprofile = UserProfile.objects.get(user=user)
    else:
        userprofile = []


    allcategory = ThreadCategory.objects.all().order_by('pid')

    if lan == 'en':
        form = ForumSearchForm_en
    if lan == 'cn':
        form = ForumSearchForm_cn            

    searched_term = ''
    displayed_category = ''
    displayed_threads = ''

    if request.method == 'POST':
        form = form(request.POST)
        # state.append('hoho1')
        if form.is_valid():

            
            cd = form.cleaned_data
            displayed_threads = ThreadContent.objects.all().order_by('-posted_on')        
            displayed_topics = []


            if int(cd['category']) > 0:
                category = int(cd['category'])
                displayed_threads = displayed_threads.filter(of_thread__category__pid=category).order_by('-posted_on')        
                displayed_category = ThreadCategory.objects.get(pid=cd['category'])
                # displayed_topics = displayed_topics.filter(category__pid=category)

            if cd['name']:
                from django.db.models import Q                
                displayed_threads = displayed_threads.filter(Q(title__icontains=cd['name'])|Q(Content__icontains=cd['name'])).order_by('-posted_on')        
                searched_term = cd['name']
                
            # for item in displayed_topics:
            #     displayed_topics = item.of_thread_set.all()

            if int(cd['language']) > 0:
                language = int(cd['language'])
                displayed_threads = displayed_threads.filter(language__pid=language).order_by('-posted_on')
                # displayed_

    

            for item in displayed_threads:
                if not (item.of_thread in displayed_topics):
                    displayed_topics.append(item.of_thread)
            
            # displayed_topics = sorted(displayed_topics, key='update_on', reverse=True)

            # displayed_topics = displayed_topics.order_by('-update_on')

            # if int(cd['level']) > 0:
            #     level = int(cd['level'])
            #     displayed_products = displayed_products.filter(level=level)

            # if int(cd['language']) > 0:
            #     language = Language.objects.filter(pid=int(cd['language']))
            #     displayed_products = displayed_products.filter(language=language)

            # if cd['I_download']:
            #     displayed_products = displayed_products.exclude(online_download=None)
    else:
        displayed_topics = Thread.objects.all().order_by('-update_on')


    return render_to_response('discussion_detailview.html',{'allcategory':allcategory, 
                                                            'displayed_topics':displayed_topics, 
                                                            'userprofile':userprofile, 
                                                            'searched_term':searched_term, 
                                                            'displayed_category':displayed_category, 
                                                            'displayed_threads':displayed_threads, 
                                                            'state':state, 'lan':lan, 'form':form}, RequestContext(request))        

# def searchresult(request, keyword, topic):



def threadcategory(request, categoryid):


    lan = setlanguage(request)

    user = request.user
    username = user.username
    if username:
        userprofile = UserProfile.objects.get(user=user)
    else:
        userprofile = []

    if lan == 'en':
        form = ForumSearchForm_en
    if lan == 'cn':
        form = ForumSearchForm_cn            

    state = []

    allcategory = ThreadCategory.objects.all().order_by('pid')


    displayed_category = allcategory.get(pid=categoryid)
    displayed_topics = Thread.objects.filter(category=displayed_category).order_by('-update_on')


    # displayed_threads = displayed_topics.of_thread_sets.all()
    # displayed_threads = ThreadContent.objects.filter(of_thread__category=displayed_category)

    displayed_threads = []
    for item in displayed_topics:
        try:
            temp = ThreadContent.objects.get(of_thread__category=item)
            if temp:
                displayed_threads.append(temp)
        except:
            pass
        

    allcontent = ThreadContent.objects.all()




    # displayed_threads = []
    # for topic in displayed_topics:
    #     if lan=='en'
    #         from django.db.models import Q                
    #         temp = displayed_thread.filter(Q(name__icontains=cd['name'])|Q(title_CN__icontains=cd['name'])|Q(title_EN__icontains=cd['name']))

    #         displayed_threads.append(temp)

    return render_to_response('discussion_detailview.html',{'allcategory':allcategory, 
                                                            'allcontent':allcontent, 
                                                            'userprofile':userprofile, 
                                                            'displayed_topics':displayed_topics, 
                                                            'displayed_category':displayed_category, 
                                                            'displayed_threads':displayed_threads, 
                                                            'state':state, 'lan':lan, 'form':form}, RequestContext(request))        







def threadresultpostedby(request, posted_by):


    lan = setlanguage(request)

    user = request.user
    username = user.username
    if username:
        userprofile = UserProfile.objects.get(user=user)
    else:
        userprofile = []

    if lan == 'en':
        form = ForumSearchForm_en
    if lan == 'cn':
        form = ForumSearchForm_cn            

    state = []

    allcategory = ThreadCategory.objects.all().order_by('pid')


    displayed_category = []
    displayed_topics = []




    displayed_threads = ThreadContent.objects.filter(posted_by__user__username=posted_by).order_by('-posted_on')

    for item in displayed_threads:
        if not (item.of_thread in displayed_topics):
            displayed_topics.append(item.of_thread)

        


    return render_to_response('discussion_detailview.html',{'posted_by':posted_by, 
                                                            'allcategory':allcategory, 
                                                            'userprofile':userprofile, 
                                                            'displayed_topics':displayed_topics, 
                                                            'displayed_category':displayed_category, 
                                                            'displayed_threads':displayed_threads, 
                                                            'state':state, 'lan':lan, 'form':form}, RequestContext(request))        










def threadresultinlanguage(request, inlanguage):


    lan = setlanguage(request)

    user = request.user
    username = user.username
    if username:
        userprofile = UserProfile.objects.get(user=user)
    else:
        userprofile = []

    if lan == 'en':
        form = ForumSearchForm_en
    if lan == 'cn':
        form = ForumSearchForm_cn            

    state = []

    allcategory = ThreadCategory.objects.all().order_by('pid')


    displayed_category = []
    displayed_topics = []




    displayed_threads = ThreadContent.objects.filter(language__name=inlanguage).order_by('-posted_on')

    for item in displayed_threads:
        if not (item.of_thread in displayed_topics):
            displayed_topics.append(item.of_thread)

        


    return render_to_response('discussion_detailview.html',{'posted_by':inlanguage, 
                                                            'allcategory':allcategory, 
                                                            'userprofile':userprofile, 
                                                            'displayed_topics':displayed_topics, 
                                                            'displayed_category':displayed_category, 
                                                            'displayed_threads':displayed_threads, 
                                                            'state':state, 'lan':lan, 'form':form}, RequestContext(request))        






    


def threadpost(request, categoryid):

    if not request.user.is_authenticated() or not request.user.is_active:               
        return HttpResponseRedirect('/homepage/')


    lan = setlanguage(request)
    user = request.user
    username = user.username
    userprofile = UserProfile.objects.get(user=user)


    if lan == 'en':
        form = ForumSearchForm_en

        form_post = ThreadPostForm(initial= {
                    'language': 1,}
                    )
    if lan == 'cn':
        form = ForumSearchForm_cn            
        form_post = ThreadPostForm(initial= {
                    'language': 2,}
                    )

    

    state = []

    allcategory = ThreadCategory.objects.all().order_by('pid')

    displayed_category = allcategory.get(pid=categoryid)



    if request.method == 'POST':
        form_post = ThreadPostForm(request.POST)
        
        if form_post.is_valid():
            if lan == 'en':
                state.append('Successfully Posted!')
            if lan == 'cn':
                state.append('成功送出!')                

            cd = form_post.cleaned_data

            language = Language.objects.get(pid=cd['language'])

            topic = Thread.objects.create(category=displayed_category, 
                                          update_on=datetime.datetime.now(),
                                          update_by=userprofile,
                                          )
            thread = ThreadContent.objects.create(title=cd['title'],
                                                  Content=cd['content'],
                                                  language=language,
                                                  posted_by=userprofile,
                                                  posted_on=datetime.datetime.now(),
                                                  of_thread=topic,
                                                  )

            url = '/discussion/category/'+categoryid+'/'
            return HttpResponseRedirect(url)    


    if displayed_category.pid == 1:
        if userprofile.master_status:
            return render_to_response('discussion_postview.html',{'allcategory':allcategory, 
                                                                  'displayed_category':displayed_category, 
                                                                  'userprofile':userprofile, 
                                                                  'state':state, 'lan':lan, 'form':form, 'form_post':form_post}, RequestContext(request))        
        else:
            if lan == 'en':
                state.append('Only masters can post questions here')
            if lan == 'cn':
                state.append('只有師父可以在此提問')
            return render_to_response('discussion_postview.html',{'allcategory':allcategory, 
                                                                  'displayed_category':displayed_category, 
                                                                  'userprofile':userprofile, 
                                                                  'state':state, 'lan':lan, 'form':form}, RequestContext(request))        
    else:
        return render_to_response('discussion_postview.html',{'allcategory':allcategory, 
                                                              'displayed_category':displayed_category, 
                                                              'userprofile':userprofile, 
                                                              'state':state, 'lan':lan, 'form':form, 'form_post':form_post}, RequestContext(request))        

def threaddetail(request, postid):

    # if not request.user.is_authenticated() or not request.user.is_active:               
        # return HttpResponseRedirect('/accounts/login/')

    lan = setlanguage(request)
    user = request.user
    username = user.username
    if username:
        userprofile = UserProfile.objects.get(user=user)
    else:
        userprofile = []


    if lan == 'en':
        form = ForumSearchForm_en

        form_post = ThreadPostForm(initial= {
                    'language': 1,}
                    )
    if lan == 'cn':
        form = ForumSearchForm_cn            
        form_post = ThreadPostForm(initial= {
                    'language': 2,}
                    )


    state = []
    allcategory = ThreadCategory.objects.all().order_by('pid')
    displayed_thread = ThreadContent.objects.get(id=postid)
    # displayed_topics = displayed_thread.of_thread
    
    displayed_topics = displayed_thread.of_thread
    all_thread = ThreadContent.objects.filter(of_thread=displayed_topics)

    available_language = []


    displayed_replies = Reply.objects.filter(following_thread=displayed_topics).order_by('-posted_on')        

    for item in all_thread:
        available_language.append(item.language)    

    return render_to_response('discussion_threaddetailview.html',{'displayed_replies':displayed_replies, 
                                                                  'userprofile':userprofile, 
                                                                  'displayed_topics':displayed_topics, 
                                                                  'available_language':available_language, 
                                                                  'allcategory':allcategory, 
                                                                  'displayed_thread':displayed_thread, 
                                                                  'state':state, 'lan':lan, 'form':form, 'form_post':form_post}, RequestContext(request))


def topiclanguagesearch(request, topicid, lanid):

    if not request.user.is_authenticated() or not request.user.is_active:               
        return HttpResponseRedirect('/homepage/')

    lan = setlanguage(request)
    user = request.user
    username = user.username
    userprofile = UserProfile.objects.get(user=user)


    if lan == 'en':
        form = ForumSearchForm_en

        form_post = ThreadPostForm(initial= {
                    'language': 1,}
                    )
    if lan == 'cn':
        form = ForumSearchForm_cn            
        form_post = ThreadPostForm(initial= {
                    'language': 2,}
                    )


    state = []
    allcategory = ThreadCategory.objects.all().order_by('pid')

    displayed_topics = Thread.objects.get(id=topicid)    
    displayed_thread = ThreadContent.objects.get(language__pid=lanid, of_thread=displayed_topics)
    # displayed_topics = displayed_thread.of_thread    
    all_thread = ThreadContent.objects.filter(of_thread=displayed_topics)

    available_language = []

    for item in all_thread:
        available_language.append(item.language)    



    url = '/discussion/thread/'+str(displayed_thread.id)+'/'
    return HttpResponseRedirect(url)    


    return render_to_response('discussion_threaddetailview.html',{'displayed_topics':displayed_topics, 
                                                                  'userprofile':userprofile,                     
                                                                  'available_language':available_language, 
                                                                  'allcategory':allcategory, 
                                                                  'displayed_thread':displayed_thread, 
                                                                  'state':state, 'lan':lan, 'form':form, 'form_post':form_post}, RequestContext(request))


def postreply(request, topicid, threadid):

    if not request.user.is_authenticated() or not request.user.is_active:               
        return HttpResponseRedirect('/homepage/')


    lan = setlanguage(request)
    user = request.user
    username = user.username
    userprofile = UserProfile.objects.get(user=user)


    if lan == 'en':
        form = ForumSearchForm_en
    if lan == 'cn':
        form = ForumSearchForm_cn

    form_post = ReplyPostForm()

    state = []

    allcategory = ThreadCategory.objects.all().order_by('pid')

    displayed_topic = Thread.objects.get(id=topicid)
    displayed_thread = ThreadContent.objects.get(id=threadid)



    if request.method == 'POST':
        form_post = ReplyPostForm(request.POST)
        
        if form_post.is_valid():
            # if lan == 'en':
            #     state.append('Successfully Posted!')
            # if lan == 'cn':
            #     state.append('成功送出!')                
            cd = form_post.cleaned_data

            thread = Reply.objects.create(following_thread=displayed_topic,
                                          # following_reply=displayed_thread,
                                          Content=cd['content'],
                                          posted_by=userprofile,
                                          posted_on=datetime.datetime.now(),
                                          )

            displayed_topic.reply_number = displayed_topic.reply_number+1
            displayed_topic.update_on=datetime.datetime.now()
            displayed_topic.update_by=userprofile
            displayed_topic.save()

            url = '/discussion/thread/'+threadid+'/'
            return HttpResponseRedirect(url)    
            
    return render_to_response('discussion_postreplyview.html',{'allcategory':allcategory, 
                                                               'displayed_topic':displayed_topic, 
                                                               'displayed_thread':displayed_thread, 
                                                               'state':state, 'lan':lan, 'form':form, 'form_post':form_post}, RequestContext(request))        




def replyreply(request, replyid, threadid):

    if not request.user.is_authenticated() or not request.user.is_active:               
        return HttpResponseRedirect('/homepage/')


    lan = setlanguage(request)
    user = request.user
    username = user.username
    userprofile = UserProfile.objects.get(user=user)


    if lan == 'en':
        form = ForumSearchForm_en
    if lan == 'cn':
        form = ForumSearchForm_cn

    form_post = ReplyPostForm()

    state = []

    allcategory = ThreadCategory.objects.all().order_by('pid')

    
    displayed_reply = Reply.objects.get(id=replyid)
    # if displayed_reply.following_thread:
    #     threadid = displayed_reply.following_thread.id
    # else:
    #     threadid = displayed_reply.following_reply.following_thread.id
    # displayed_thread = ThreadContent.objects.filter()

    displayed_topic = ThreadContent.objects.get(id=threadid).of_thread

    if request.method == 'POST':
        form_post = ReplyPostForm(request.POST)
        
        if form_post.is_valid():
            # if lan == 'en':
            #     state.append('Successfully Posted!')
            # if lan == 'cn':
            #     state.append('成功送出!')                
            cd = form_post.cleaned_data

            thread = Reply.objects.create(following_reply=displayed_reply,
                                          # following_reply=displayed_thread,
                                          Content=cd['content'],
                                          posted_by=userprofile,
                                          posted_on=datetime.datetime.now(),
                                          )

            displayed_topic.reply_number = displayed_topic.reply_number+1
            displayed_topic.update_on=datetime.datetime.now()
            displayed_topic.update_by=userprofile
            displayed_topic.save()

            url = '/discussion/thread/'+str(threadid)+'/'
            return HttpResponseRedirect(url)    

            
            
    return render_to_response('discussion_postreplyview.html',{'allcategory':allcategory, 
                                                               # 'displayed_topic':displayed_topic, 
                                                               'threadid':threadid,
                                                               'displayed_thread':displayed_reply, 
                                                               'state':state, 'lan':lan, 'form':form, 'form_post':form_post}, RequestContext(request))        






def threadtranslate(request, topicid, threadid):

    if not request.user.is_authenticated() or not request.user.is_active:               
        return HttpResponseRedirect('/homepage/')


    lan = setlanguage(request)
    user = request.user
    username = user.username
    userprofile = UserProfile.objects.get(user=user)


    if lan == 'en':
        form = ForumSearchForm_en
        form_post = ThreadPostForm()
    if lan == 'cn':
        form = ForumSearchForm_cn
        form_post = ThreadPostForm()
    
    state = []

    if userprofile.translator_status:



        allcategory = ThreadCategory.objects.all().order_by('pid')

        displayed_topic = Thread.objects.get(id=topicid)
        displayed_thread = ThreadContent.objects.get(id=threadid)



        if request.method == 'POST':
            form_post = ThreadPostForm(request.POST)
            
            if form_post.is_valid():
                # if lan == 'en':
                #     state.append('Successfully Posted!')
                # if lan == 'cn':
                #     state.append('成功送出!')                
                cd = form_post.cleaned_data



                language = Language.objects.get(pid=cd['language'])                

                topic = Thread.objects.get(id=topicid)

                for item in ThreadContent.objects.filter(of_thread=topic):
                    if item.language == language:
                        state.append('language existed!')
                        return render_to_response('discussion_translatepostview.html',{'allcategory':allcategory, 
                                                                                           'displayed_topic':displayed_topic, 
                                                                                           'displayed_thread':displayed_thread, 
                                                                                           'state':state, 'lan':lan, 'form':form, 'form_post':form_post}, RequestContext(request))                                


                thread = ThreadContent.objects.create(title=cd['title'],
                                      Content=cd['content'],
                                      language=language,
                                      posted_by=userprofile,
                                      posted_on=datetime.datetime.now(),
                                      of_thread=topic,
                                      )

                url = '/discussion/thread/'+threadid+'/'
                return HttpResponseRedirect(url)    
                
        return render_to_response('discussion_translatepostview.html',{'allcategory':allcategory, 
                                                                   'displayed_topic':displayed_topic, 
                                                                   'displayed_thread':displayed_thread, 
                                                                   'state':state, 'lan':lan, 'form':form, 'form_post':form_post}, RequestContext(request))        
    else:
        state.append('For translators only!')
        url = '/discussion/thread/'+threadid+'/'
        return HttpResponseRedirect(url)            


        

def threaddelete(request, topicid):

    if not request.user.is_authenticated() or not request.user.is_active or not request.user.is_superuser:               
        return HttpResponseRedirect('/homepage/')

    lan = setlanguage(request)
    user = request.user
    username = user.username
    if username:
        userprofile = UserProfile.objects.get(user=user)
    else:
        userprofile = []


    if lan == 'en':
        form = ForumSearchForm_en

        # form_post = ThreadPostForm(initial= {
        #             'language': 1,}
        #             )
    if lan == 'cn':
        form = ForumSearchForm_cn            
        # form_post = ThreadPostForm(initial= {
        #             'language': 2,}
        #             )


    topic = Thread.objects.get(id=topicid)
        
    reply = Reply.objects.filter(following_thread=topic)    
    for item in reply:
        ror = Reply.objects.filter(following_reply=item)
        for subitem in ror:
            subitem.delete()
        item.delete()

    thread = ThreadContent.objects.filter(of_thread=topic)
    for item in thread:        
        item.delete()        

    topic.delete()


    # related_thread = 

    state = []
    allcategory = ThreadCategory.objects.all().order_by('pid')
    # displayed_thread = ThreadContent.objects.get(id=postid)
    # displayed_topics = displayed_thread.of_thread
    
    # displayed_topics = displayed_thread.of_thread
    # all_thread = ThreadContent.objects.filter(of_thread=displayed_topics)

    available_language = []


    # displayed_replies = Reply.objects.filter(following_thread=displayed_topics).order_by('-posted_on')        

    # for item in all_thread:
    #     available_language.append(item.language)    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render_to_response('discussion_threaddetailview.html',{'displayed_replies':displayed_replies, 
                                                                  'userprofile':userprofile, 
                                                                  'displayed_topics':displayed_topics, 
                                                                  'available_language':available_language, 
                                                                  'allcategory':allcategory, 
                                                                  'displayed_thread':displayed_thread, 
                                                                  'state':state, 'lan':lan, 'form':form, 'form_post':form_post}, RequestContext(request))





def masterreply(request, threadid):

    if not request.user.is_authenticated() or not request.user.is_active:               
        return HttpResponseRedirect('/homepage/')


    lan = setlanguage(request)
    user = request.user
    username = user.username
    userprofile = UserProfile.objects.get(user=user)


    if lan == 'en':
        form = ForumSearchForm_en
    if lan == 'cn':
        form = ForumSearchForm_cn

    form_post = ReplyPostForm()

    state = []

    allcategory = ThreadCategory.objects.all().order_by('pid')

    displayed_thread = ThreadContent.objects.get(id=threadid)



    if request.method == 'POST':
        form_post = ReplyPostForm(request.POST)
        
        if form_post.is_valid():
            # if lan == 'en':
            #     state.append('Successfully Posted!')
            # if lan == 'cn':
            #     state.append('成功送出!')                

            cd = form_post.cleaned_data
            displayed_thread.master_content = cd['content']
            displayed_thread.replied_by = userprofile
            displayed_thread.replied_on = datetime.datetime.now()
            displayed_thread.save()

            url = '/discussion/thread/'+threadid+'/'
            return HttpResponseRedirect(url)    
            
    return render_to_response('discussion_postreplyview.html',{'allcategory':allcategory, 
                                                               'displayed_thread':displayed_thread, 
                                                               'state':state, 'lan':lan, 'form':form, 'form_post':form_post}, RequestContext(request))        

