from django.shortcuts import render
from Posts.models import Posts

def home(request):
    data= Posts.objects.all()
    return render(request, 'home.html',{'data':data})