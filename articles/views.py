from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .scripts.sluggify import sluggify
import datetime

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', { 'articles': articles })

def article_detail(request, slug):
    #return HttpResponse(slug)
    #Query db.sqlite3 to check whether or not slug is present: return article if True; return 404 if False
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', { 'article':article })

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # Save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.slug = sluggify(instance.title)
            notvalid = len(Article.objects.all().filter(slug=instance.slug))
            while len(Article.objects.all().filter(slug=instance.slug)) != 0:
                instance.slug += "-a"
            instance.save()
            return redirect("articles:list")
    else:
        form = forms.CreateArticle()
    return render(request, "articles/article_create.html", { 'form':form })
