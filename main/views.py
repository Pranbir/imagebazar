import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .data import *


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the main app index.")


def home(request):
    if request.method == "GET":
        #data = json.loads(get_all_images())
        data = get_all_images()
        return render(request,'home.html',{"data" : data , "categories": get_ten_categories()})
    else:
        return JsonResponse({"status":"error" , "error":"Methods not allowed"}, status=405)


def search(request):
    if request.method == "GET":
        #data = json.loads(get_all_images())
        q = request.GET.get('q', None)
        data = get_all_images(q=q)
        return render(request,'home.html',{"data" : data, "q":q , "categories": get_ten_categories()})
    else:
        return JsonResponse({"status":"error" , "error":"Methods not allowed"}, status=405)


def category(request, id):
    if request.method == "GET":
        #data = json.loads(get_all_images())
        data = get_all_images(cat_id=id)
        return render(request,'home.html',{"data" : data , "categories": get_ten_categories()})
    else:
        return JsonResponse({"status":"error" , "error":"Methods not allowed"}, status=405)

