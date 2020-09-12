from django.urls import path

from . import views

urlpatterns = [
    path('', views.home , name='Homepage'),
    path('category/<id>', views.category , name='Category'),
    path('search', views.search , name='Search')
]
