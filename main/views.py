from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the main app index.")


def home(request):
    return render(request,'home.html',{})


def search(request):
    return render('ff.html')


def category(request):
    return render('ff.html')


def single_image(request):
    return render('ff.html')