from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Address(models.Model):
    address=models.CharField(max_length=300)
    
    def __str__(self):
        return self.address
    
class School(models.Model):
    name=models.CharField(max_length=300)
    estd_date=models.DateField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=200)
    address=models.ForeignKey(Address,on_delete=models.DO_NOTHING,blank=True,null=True)
    school=models.ForeignKey(School,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Students'
        
    

class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE,null=True)  # Add this line
    photo = models.ImageField(null=True, blank=True, upload_to='Student_Profile_pic')
    PP_name = models.CharField(max_length=50, null=True, blank=True)
    desc = models.TextField()

