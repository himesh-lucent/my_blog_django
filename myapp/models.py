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