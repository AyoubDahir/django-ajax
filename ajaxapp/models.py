from django.db import models

# Create your models here.

class patient(models.Model):
    fullname=models.CharField(max_length=100);
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    date_created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname
    
    
    
