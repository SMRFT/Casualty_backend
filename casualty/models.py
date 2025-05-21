from django.db import models

from django.db import models
from django.contrib.auth.models import User


from django.db import models
from django.utils.timezone import now


class AuditModel(models.Model):
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    lastmodified_by = models.CharField(max_length=100, blank=True, null=True)
    lastmodified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.created_by:
            self.created_by = "system"
        self.lastmodified_by = self.lastmodified_by or "system"
        super().save(*args, **kwargs)

class Patient(AuditModel):
    
    name = models.CharField(max_length=200,blank=True)
    erNumber = models.CharField(max_length=100,blank=True)
    billNumber = models.CharField(max_length=100)
    doctorName = models.CharField(max_length=200,blank=True)
    billDate = models.DateField()
    opNumber = models.CharField(max_length=100,blank=True)
    billType = models.CharField(max_length=150,blank=True)
    age =  models.CharField(max_length=100,blank=True)
    gender = models.CharField(max_length=10,blank=True)
    dob =  models.CharField(max_length=100,blank=True)
    address =  models.CharField(max_length=100,blank=True)
    totalAmount=  models.CharField(max_length=100,blank=True)
    discount=  models.CharField(max_length=100,blank=True)
    discountedAmount=  models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name
    


# models.py

from django.db import models

class PatientRegister(AuditModel):
    
    name = models.CharField(max_length=255)
    dob =  models.CharField(max_length=100,blank=True)
    age =models.CharField(max_length=100,blank=True)
    gender = models.CharField(max_length=10)
    permanentAddress = models.TextField(blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobilePhone = models.CharField(max_length=20)
    homePhone = models.CharField(max_length=20, blank=True, null=True)
    bloodGroup = models.CharField(max_length=5, blank=True, null=True)
    spouseName = models.CharField(max_length=255, blank=True, null=True)
    referredBy = models.CharField(max_length=255, blank=True, null=True)
    doctorName = models.CharField(max_length=255, blank=True, null=True)



# models.py
from django.db import models

class Employee(models.Model):
    empid = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords in production

    def __str__(self):
        return self.name


    
