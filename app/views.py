from django.http import HttpResponse
from django.shortcuts import render
from app.models import Blog
# Create your views here.
def home(request):
    return render(request,'index.html')

def blog(request):
    blogs=Blog.objects.all()
    context={'blogs':blogs}
    return render(request,'bloghome.html',context)

def contact(request):
    return render(request,'contact.html')


def blogpost(request,slug):
    return HttpResponse(f"you are viweing {slug}")

def search(request):
    return render(request,'search.html')