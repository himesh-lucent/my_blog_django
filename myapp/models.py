from django.db import models

# Create your models here.

class Students(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.CharField(max_length=50)
    image = models.ImageField(upload_to='studentsimage')

    def __str__(self):
        return self.fname + " " + self.lname + " " + str(self.age) + " " + self.course
    
class Contact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return self.fname + " " + self.lname
    

class Course(models.Model):
    cname = models.CharField(max_length=50)
    cdesc = models.CharField(max_length=255)
    cimage = models.ImageField(upload_to='courseimage')

    def __str__(self):
        return self.cname