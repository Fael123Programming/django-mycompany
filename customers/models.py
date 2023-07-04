from django.db import models

class PhoneNumber(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=False)
    value = models.CharField(max_length=30, null=False)
    

class Email(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=False)
    value = models.CharField(max_length=150, null=False)
    
    
class Address(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=False)
    country = models.CharField(max_length=150, null=True)
    state_province = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=150, null=True)
    street = models.CharField(max_length=150, null=True)
    number = models.CharField(max_length=10, null=True)
    
    
class Customer(models.Model):
    name = models.CharField(max_length=150, null=False)
    phone_number = models.ForeignKey('PhoneNumber', on_delete=models.RESTRICT, null=False)
    email = models.ForeignKey('Email', on_delete=models.RESTRICT, null=False)
    address = models.ForeignKey('Address', on_delete=models.RESTRICT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
