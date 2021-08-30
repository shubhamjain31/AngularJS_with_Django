from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname 			= models.CharField(max_length=100, blank=True, null=True)
    first_name			= models.CharField(max_length=64, blank=True, null=True)
    last_name			= models.CharField(max_length=64, blank=True, null=True)
    email				= models.EmailField()
    emp_code 			= models.CharField(max_length=3, blank=True, null=True)
    mobile				= models.CharField(max_length=15, blank=True, null=True)
    joining_date 		= models.DateTimeField(auto_now_add=True, null=True)
    position			= models.ForeignKey(Position,on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname