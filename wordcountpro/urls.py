
from . import views 
from django.urls import path

urlpatterns = [
    path('' , views.homepage  , name='home'),
    path('count/', views.count , name='count'),
    path('aboutpage' , views.about , name='about'),
]
