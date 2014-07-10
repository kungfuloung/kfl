# -*- coding: utf-8 -*-

from django.template.loader import get_template
from django.shortcuts import render
from django.contrib import auth
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required  

from django.utils.translation import ugettext as _


import datetime

from product.models import UserProfile, DVDProduct, Language, ProductCategory, ProductBundle
from product.forms import ProductSearchForm_en, ProductSearchForm_cn

from discussion.models import ThreadContent, Thread
# Create your views here.

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login(request):
      
    # try:
    #     # lan = request.session['django_language']
    #     lan = 'cn'
    # except:
    #     lan = 'en'
    lan = setlanguage(request)

    if not request.user.is_active:
        # if lan == 'en':
        #     state = "Please log in below..."
        # if lan == 'cn':
        #     state = "請登入網站..."
        state = ''
        username = password = ''
        user = auth.authenticate(username=username, password=password)            
        

        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = auth.authenticate(username=username, password=password)            
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    state = "You're successfully logged in!"
                    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    # try:
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))                        
                    # except:
                    # return HttpResponseRedirect('/accounts/personal_information')
                else:
                    if lan == 'en':
                        state = "Your account is not active, please contact the site admin."                
                    if lan == 'cn':
                        state = "您的帳號未被啟用, 請聯絡網管人員"                                        
            else:
                if lan == 'en':
                    state = "your username and/or password were incorrect."
                if lan == 'cn':
                    state = "您輸入的使用者名稱或密碼有錯誤"

        return render_to_response('login_form.html',{'state':state, 'username':username, 'user':user, 'lan':lan}, RequestContext(request))
    else:
        
        user = request.user        
        
        state = "You're logged in!"                
        # auth.login(request, user)
        # return render_to_response('login_form.html',{'state':state, 'user':user}, RequestContext(request))
        # try:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))            
        # except:
        # return HttpResponseRedirect('/accounts/personal_information')
        
        # return render_to_response('/accounts/personal_information', {'state':state, 'user':user, 'UserProfile':userprofile})

        # return render_to_response('login_form.html',{'state':state, 'user':user}, RequestContext(request))
    # return render_to_response('login_form.html',{'state':state, 'username':username, 'user':user}, RequestContext(request))



def logout(request):

    lan = setlanguage(request)

    try:
        del request.session['member_id']
    except KeyError:
        pass
    # return HttpResponse("You're logged out.")     
    auth.logout(request)   
    if lan == 'en':
        state = "You're logged out."
    if lan == 'cn':
        state = "您已登出."        
    username = password = ''
    user = auth.authenticate(username=username, password=password)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return render_to_response('login_form.html',{'state':state, 'username':username, 'user':user, 'lan':lan}, RequestContext(request))



# @login_required
def personal_information(request):
    
    

    lan = setlanguage(request)

    if not request.user.is_active:
        # return HttpResponseRedirect('/accounts/login')
        return HttpResponseRedirect('/homepage/')

    state = "You're logged in."
    # username = password = ''
    # user = auth.authenticate(username=username, password=password)
    user = request.user
    username = user.username
    userprofile = UserProfile.objects.get(user=user)


    # if userprofile.master_status or userprofile.translator_status:
    if userprofile.master_status:
        thread_not_replied = ThreadContent.objects.filter(master_content=None)
    else:
        thread_not_replied = []

    thread_not_translated = []

    # A slacking way of filtering out, works only when two languages are possible
    if userprofile.translator_status:
        for item in Thread.objects.all():
            try: 
                temp = ThreadContent.objects.get(of_thread=item)
                thread_not_translated.append(temp)
            except:
                pass
                
    

    return render_to_response('personal_information.html',{'userprofile':userprofile, 
                                                           'thread_not_replied':thread_not_replied,
                                                           'thread_not_translated':thread_not_translated,
                                                           'state':state, 'username':username, 'user':user, 'lan':lan}, RequestContext(request))
    # else:
    #     return render_to_response('homepage.html',{'userprofile':userprofile, 'state':state, 'username':username, 'user':user, 'lan':lan}, RequestContext(request))




def overview(request):

    lan = setlanguage(request)


    if lan == 'en':
        form = ProductSearchForm_en
    if lan == 'cn':
        form = ProductSearchForm_cn            

    state = []

    allcategory = ProductCategory.objects.all()
    allbundled = ProductBundle.objects.all()

    if request.method == 'POST':
        form = form(request.POST)
        # state.append('hoho1')
        if form.is_valid():
            
            cd = form.cleaned_data
            displayed_products = DVDProduct.objects.all()        
            


            if int(cd['category']) > 0:
                category = int(cd['category'])
                displayed_products = displayed_products.filter(category__pid=category)

            if cd['name']:
                from django.db.models import Q                
                displayed_products = displayed_products.filter(Q(name__icontains=cd['name'])|Q(title_CN__icontains=cd['name'])|Q(title_EN__icontains=cd['name']))

            if int(cd['level']) > 0:
                level = int(cd['level'])
                displayed_products = displayed_products.filter(level=level)

            if int(cd['language']) > 0:
                language = Language.objects.filter(pid=int(cd['language']))
                displayed_products = displayed_products.filter(language=language)

            if cd['I_download']:
                displayed_products = displayed_products.exclude(online_download=None)



            # else:
            #     displayed_products = DVDProduct.objects.all()        

            # displayed_products = DVDProduct.objects.all()                

            displayed_bundle = []

            # displayed_bund = allbundled.filter(products=displayed_products)
            for bundle in allbundled:
                for item in displayed_products:
                    if bundle.products.all().filter(name=item.name) and not(bundle in displayed_bundle):
                        # displayed_bundle.append
                    # allbundled.filter(products=item):
                        displayed_bundle.append(bundle)
                        break
                
            
    else:
        displayed_products = DVDProduct.objects.all()
        displayed_bundle = ProductBundle.objects.all()

    if displayed_products:
        return render_to_response('product_overview.html',{'displayed_bundle':displayed_bundle, 'allcategory':allcategory, 'displayed_products':displayed_products, 'state':state, 'lan':lan, 'form':form}, RequestContext(request))        
    else:
        if lan == 'en':
            state.append('No corresponding products in the database')
        if lan == 'cn':
            state.append('無符合條件的商品')

        return render_to_response('product_overview.html',{'allcategory':allcategory, 'state':state, 'lan':lan, 'form':form}, RequestContext(request))


def productcategory(request, categoryid):


    lan = setlanguage(request)


    if lan == 'en':
        form = ProductSearchForm_en
    if lan == 'cn':
        form = ProductSearchForm_cn            

    state = []

    allcategory = ProductCategory.objects.all()    

    displayed_category = allcategory.get(pid=categoryid)
    displayed_products = DVDProduct.objects.filter(category=displayed_category)

    allbundled = ProductBundle.objects.all()
    displayed_bundle = []
    # displayed_bund = allbundled.filter(products=displayed_products)
    for bundle in allbundled:
        for item in displayed_products:
            if bundle.products.all().filter(name=item.name) and not(bundle in displayed_bundle):
                # displayed_bundle.append
            # allbundled.filter(products=item):
                displayed_bundle.append(bundle)
                break
        

    # if request.method == 'POST':
    #     form = form(request.POST)
    #     # state.append('hoho1')
    #     if form.is_valid():
            
    #         cd = form.cleaned_data
    #         displayed_products = DVDProduct.objects.all()        
                
    #         if int(cd['category']) > 0:
    #             category = int(cd['category'])
    #             displayed_products = displayed_products.filter(category__pid=category)

    #         if cd['name']:
    #             from django.db.models import Q                
    #             displayed_products = displayed_products.filter(Q(name__icontains=cd['name'])|Q(title_CN__icontains=cd['name'])|Q(title_EN__icontains=cd['name']))

    #         if int(cd['level']) > 0:
    #             level = int(cd['level'])
    #             displayed_products = displayed_products.filter(level=level)

    #         if int(cd['language']) > 0:
    #             language = Language.objects.filter(pid=int(cd['language']))
    #             displayed_products = displayed_products.filter(language=language)

    #         if cd['I_download']:
    #             displayed_products = displayed_products.exclude(online_download=None)



    #         # else:
    #         #     displayed_products = DVDProduct.objects.all()        

    #         # displayed_products = DVDProduct.objects.all()                            

    # if displayed_products:
    return render_to_response('product_overview.html',{'displayed_bundle': displayed_bundle, 'allcategory':allcategory, 'displayed_products':displayed_products, 'state':state, 'lan':lan, 'form':form}, RequestContext(request))        
    # else:
    #     if lan == 'en':
    #         state.append('No corresponding products in the database')
    #     if lan == 'cn':
    #         state.append('無符合條件的商品')

        # return render_to_response('product_overview.html',{'allcategory':allcategory, 'state':state, 'lan':lan, 'form':form}, RequestContext(request))





def productview(request, productname):

    lan = setlanguage(request)
    state = []
    # try:
    product = DVDProduct.objects.get(name=productname)
    # product = DVDProduct.objects.get(name='productname')
    # except:
    #     pass        

    
    return render_to_response('product_detailview.html',{'state':state, 'lan':lan, 'product':product}, RequestContext(request))
    

def productbundleview(request, bundleid):

    lan = setlanguage(request)
    state = []
    # try:
    displayed_bundle = ProductBundle.objects.get(id=bundleid)

    allcategory = ProductCategory.objects.all()
    
    if lan == 'en':
        form = ProductSearchForm_en
    if lan == 'cn':
        form = ProductSearchForm_cn            

    
    # return render_to_response('bundle_detailview.html',{'state':state, 'lan':lan, 'bundle':bundle}, RequestContext(request))
    return render_to_response('bundle_detailview.html',{'displayed_bundle': displayed_bundle, 'allcategory':allcategory, 'state':state, 'lan':lan, 'form':form}, RequestContext(request))        


def set_cn(request):
    request.session['django_language'] = 'cn'
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def set_en(request):
    request.session['django_language'] = 'en'
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    

def setlanguage(request):
    try:
        return request.session['django_language']
    except:
        return 'en'


def homepage(request):

    lan = setlanguage(request)


    if lan == 'en':
        form = ProductSearchForm_en
    if lan == 'cn':
        form = ProductSearchForm_cn            

    state = []

    user = request.user



    return render_to_response('homepage.html',{'state':state, 'user':user, 'lan':lan}, RequestContext(request))