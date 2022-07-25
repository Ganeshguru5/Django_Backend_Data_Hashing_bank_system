from multiprocessing.spawn import old_main_modules
from pyexpat import model
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.fields import BooleanField, CharField
from django.db.models.fields.files import ImageField
from twilio.rest.api.v2010 import account



# Create your models here.


class savingsLogin(models.Model):
    nameonpassbook=models.CharField(max_length=100)
    birthdate=models.DateField()
    accnumber=models.CharField(max_length=15)
    mobnumber=models.CharField(max_length=10)

class ATMLogin(models.Model):
    ATMnumber=models.CharField(max_length=20)
    mobnum=models.CharField(max_length=10)

class OBLogin(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
    mobnum=models.CharField(max_length=10)

class Customer_details(models.Model):
    photo=ImageField(upload_to='photos')
    Firstname=CharField(max_length=100)
    Lastname=CharField(max_length=100)
    emailid=CharField(max_length=100)
    nameonpassbook=models.CharField(max_length=100)
    birthdate=models.DateField()
    accnumber=models.CharField(max_length=15)
    bank_name=models.CharField(max_length=100)
    ATMnumber=models.CharField(max_length=20)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
    mobnum=models.CharField(max_length=10)
    adharcardimg=models.ImageField(upload_to='adhar_proof')
    voteridimg=models.ImageField(upload_to='voterid_proof')
    adharnum=models.CharField(max_length=15)
    voteridnum=models.CharField(max_length=10)
    accountbalance=models.CharField(max_length=10)
    atmcard=models.BooleanField(default=False)
    debitcard=models.BooleanField(default=False)
    pin=models.CharField(max_length=5)
    ob_registered=BooleanField(default=False)
    country=models.CharField(max_length=100)
    accounttype=models.CharField(max_length=100)
    bank_ifsc_code=models.CharField(max_length=100)
    bank_branch_code=models.CharField(max_length=100)

class linkedAccounts(models.Model):
    accnumber=models.CharField(max_length=100)  
    linkedaccnumber=models.CharField(max_length=100)  
    accounttype=models.CharField(max_length=100)
    bank_name=models.CharField(max_length=100)  
    bank_ifsc_code=models.CharField(max_length=100)  
    bank_branch_code=models.CharField(max_length=100) 
    country=models.CharField(max_length=100)  
    bank_location=models.CharField(max_length=100)

class transactionHistory(models.Model):
    accnumber = models.CharField(max_length=100)
    second_acc = models.CharField(max_length=100)
    amounttransfered = models.CharField(max_length=100)
    transactiontype = models.CharField(max_length=100)
    fees = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
   
    

# class TransactionHistory(models.Model):
#     person1=models.CharField(max_length=100)
#     accountnum1=models.CharField(max_length=15)
#     person2=models.CharField(max_length=100)
#     accountnum2=models.CharField(max_length=15)
#     amount=models.CharField(max_length=10)
    



    