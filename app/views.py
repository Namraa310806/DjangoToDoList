from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'bloghome.html')

def contact(request):
    return render(request,'contact.html')


def blogpost(request,slug):
    return HttpResponse(f"you are viweing {slug}")

def search(request):
    return render(request,'search.html')