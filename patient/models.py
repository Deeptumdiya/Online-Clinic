from django.db import models

class Patient(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.TextField()
    mob=models.IntegerField()
    age=models.IntegerField()
    gen=models.CharField(max_length=50)
    dis=models.TextField()

class Appointment(models.Model):
    dname=models.TextField()
    pname=models.TextField()
    date=models.TextField()
    time=models.TextField()
    pres=models.TextField()

