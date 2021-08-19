from django.urls import path
from .views import main,home


urlpatterns = [
    path('',main.as_view()),
    path('home',home.as_view())

]
