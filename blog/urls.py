from django.urls import path
from blog import views


urlpatterns = [
    path('',views.bloghome),
    path('<str:slug>',views.blogpost),
    
]