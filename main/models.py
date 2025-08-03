from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    des = models.TextField()

    def __str__(self):
        return self.title

class School(models.Model):
    name = models.CharField(max_length=200)
    estd = models.DateField()

    def __str__(self):
        return self.name
    
class Address(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class meta:
        verbose_name_plular= "Addresses"
    

class Grade(models.Model):
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING, null=True)
    cname = models.CharField(max_length=20)
    section= models.CharField(max_length=10)

    def __str__(self):
        return f"{self.school} | {self.cname}"

class Student(models.Model):
    school = models.ForeignKey(School,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=150)
    roll_num = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name   
    
class SudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)
    description= models.CharField(max_length=500)
    profile_image= models.ImageField(upload_to="student_profile", null=True, blank=True)

    def __str__(self):
        return f"{self.student} 's pOFILE pic "

class Parent(models.Model):
    name = models.CharField(max_length=200)

    Children = models.ManyToManyField(Student)

    def __str__(self):
        return self.name