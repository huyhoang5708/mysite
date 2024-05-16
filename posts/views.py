from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Post
# Create your views here.

def posts(request):
    data=list(Post.objects.all().values())

    return render(request, "home.html",{
        "posts": data
    })

def product_detail(request, product_slug):
    product_slug = Post.objects.get(slug=product_slug)
    return render(request, 'product_detailed.html', {"product_slug": product_slug,
                                                    })