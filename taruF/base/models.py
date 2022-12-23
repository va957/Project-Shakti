from pyexpat import model
from django.db import models
import datetime

from psycopg2 import Date
            

class RMP(models.Model):
    name = models.CharField(max_length=200, null=True)
    email= models.EmailField(unique=True, null=True)
    phone =models.PositiveBigIntegerField(null=True)
    pincode=models.PositiveIntegerField(null=True)
    USERNAME_FIELD='name'
    REQUIRED_FIELDS=[name,email,phone,pincode]

class Patient(models.Model):
    name = models.CharField(max_length=200, null=True)
    aadharnum=models.PositiveIntegerField(null=True,max_length=16)
    address = models.CharField(max_length=200, null=True)
    pincode=models.PositiveIntegerField(null=True)
    phone =models.PositiveBigIntegerField(null=True)
    marital_status = models.BooleanField(default=False)
    sex = models.BooleanField(default=False)
    age = models.PositiveSmallIntegerField(null = True)
    height = models.PositiveSmallIntegerField(null = False,default=145)
    weight = models.PositiveSmallIntegerField(null = False,default=45)
    USERNAME_FIELD='name'
    REQUIRED_FIELDS=[name,aadharnum,pincode]



class Vitals(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    rmp = models.ForeignKey(RMP, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    temperature = models.PositiveSmallIntegerField(null=True)
    high_bp = models.PositiveSmallIntegerField(null=True)
    low_bp = models.PositiveSmallIntegerField(null=True)
    pulse = models.PositiveSmallIntegerField(null=True)
    respiration = models.PositiveSmallIntegerField(null=True)
    oxygen_saturation = models.PositiveSmallIntegerField(null=True)
    

class Doctor(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    aadharnum=models.PositiveIntegerField(null=True,max_length=16)
    pincode=models.PositiveIntegerField(null=True)
    password=models.CharField(max_length=200, null=True)
    specilization = models.CharField(max_length=200, null=True)
    USERNAME_FIELD='name'
    REQUIRED_FIELDS=[name,email,aadharnum,pincode]



class Slots(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False)
    available = models.BooleanField(default=True)
    def __str__(self):
        return str(self.date)

class Appointments(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Slot = models.ForeignKey(Slots, on_delete=models.CASCADE)
    Symptoms=models.CharField(max_length=200, null=True)
    Date=models.DateTimeField(null=False)
    
    

class medicines(models.Model):
    name=models.CharField(max_length=200, null=True)
    interval=models.PositiveIntegerField(null=True)
    Dosage=models.PositiveIntegerField(null=True)
    Appointments=models.ForeignKey(Appointments,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Prescription(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Appointments=models.ForeignKey(Appointments,on_delete=models.CASCADE)
    Medicine=models.ForeignKey(medicines,on_delete=models.CASCADE)
    Diagonosis=models.CharField(max_length=200, null=True)
    Remarks=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.Diagonosis


