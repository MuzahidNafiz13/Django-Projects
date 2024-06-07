from django.shortcuts import render
from Posts.models import Posts
from Categories.models import Category

def home(request, category_slug=None):
    data= Posts.objects.all()
    if category_slug is not None:
        category=Category.objects.get(slug=category_slug)
        data=Posts.objects.filter(category=category)
    catagories= Category.objects.all()
    return render(request, 'home.html',{'data':data, 'category': catagories})