# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    posts = Article.objects.all()
    tags=[x.category for x in posts]
    tags=list(set(tags))
    
    paginator_ = Paginator(posts, 10) 
    page = request.GET.get('page')
    try :
        post_list = paginator_.page(page)
    except PageNotAnInteger :
        post_list = paginator_.page(1)
    except EmptyPage :
        post_list = Article.objects.all()
    return render(request, 'home2.html', {'post_list' : post_list,'tags':tags,'paginator_':paginator_})

def pages(request,id):
    posts = Article.objects.all()
    
    tags=[x.category for x in posts]
    tags=list(set(tags))
    paginator = Paginator(posts, 10) 
    
    try :
        post_list = paginator.page(id)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home2.html', {'post_list' : post_list,'tags':tags,'paginator_':paginator})

def detail(request, id):
    try:
        post_list = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    posts = Article.objects.all()
    tags=[x.category for x in posts]
    tags=list(set(tags))
    
    paginator_ = Paginator(posts, 10)
    return render(request, 'post2.html', {'post_list' : post_list,'tags':tags,'paginator_':paginator_})

def archives(request) :
    posts = Article.objects.all()
    tags=[x.category for x in posts]
    tags=list(set(tags))
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 
                                            'error' : False,'tags':tags})


def search_tag(request, tag) :
    posts = Article.objects.all()
    tags=[x.category for x in posts]
    tags=list(set(tags))
    try:
        post_list = Article.objects.filter(category = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list,'tags':tags})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home2.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')



