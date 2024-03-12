from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about),
    path('students',views.students),
    path('contact',views.contact),
]