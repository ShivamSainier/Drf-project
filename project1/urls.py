from django.urls import path
from .views import main,home,index,create


urlpatterns = [
    path('',main.as_view()),
    path('home',home.as_view()),
    path('index',index),
    path('create',create.as_view())

]
