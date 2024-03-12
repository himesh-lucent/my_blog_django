from django.shortcuts import render, HttpResponse
from myapp.models import Students

# Create your views here.
def home(request):
    # return HttpResponse('This is my home page')
    return render(request,'home.html')

def about(request):
    # return HttpResponse('This is my about page')
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

def students(request):
    all_students = Students.objects.all()
    return render(request, 'students.html',{'students':all_students})