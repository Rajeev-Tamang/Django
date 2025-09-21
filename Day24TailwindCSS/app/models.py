from django.db import models
# Create your models here.

class studentReg(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name