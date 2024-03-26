from django.shortcuts import render, HttpResponse
from myapp.models import Students, Contact, Course

# Create your views here.
def home(request):
    # return HttpResponse('This is my home page')
    return render(request,'myapp/home.html')

def about(request):
    # return HttpResponse('This is my about page')
    return render(request,'myapp/about.html')

def courses(request):
    all_courses = Course.objects.all()
    return render(request,'myapp/courses.html',{'courses':all_courses})

def contact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        studetails = Contact(fname=fname, lname=lname, email=email, contact=contact)
        studetails.save()
    return render(request, 'myapp/contact.html')

def students(request):
    all_students = Students.objects.all()
    return render(request, 'myapp/students.html',{'students':all_students})