from django.core import serializers
from .models import *

def get_all_images(cat_id=None, q=None):
    if cat_id:
        data = list(Image.objects.filter(cat=cat_id).order_by('-insert_date').values())
    elif q:
        data = list(Image.objects.filter(title__icontains=q).order_by('-insert_date').values())
    else:
        data = list(Image.objects.all().order_by('-insert_date').values())
    return data

def get_ten_categories():
    data = list(Category.objects.all().order_by('?')[:9].values())
    return data