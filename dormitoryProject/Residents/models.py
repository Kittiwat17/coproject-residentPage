# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from unittest.util import _MAX_LENGTH
import dormitoryProject

# Create your models here.


# Create your models here.
class Resident(models.Model):
    # resident_id = models.AutoField(primary_key=True, verbose_name='resident_id', db_column='resident_id')
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.fname
    
class Comment(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=50)
    resident_resident_id = models.ForeignKey(Resident, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Contract(models.Model):
    # contract_id = models.AutoField(primary_key=True, verbose_name='contract_id', db_column='contract_id')
    desc_contract = models.TextField()
    dorm_rule = models.TextField()
    room_rate = models.FloatField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    resident_resident_id = models.ForeignKey(Resident, on_delete=models.CASCADE)

    

class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=50) #choice
    vehicle_gen = models.CharField(max_length=255)
    contract_contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    

class Invoice(models.Model):
    # invoice_id = models.AutoField(primary_key=True)
    inv_date = models.DateField(auto_now=False, auto_now_add=False)
    month_no = models.IntegerField() #choice
    room_rate = models.FloatField()
    water_ex = models.FloatField()
    elec_ex = models.FloatField()
    contract_contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    
class Expense(models.Model):
    # exp_no = models.IntegerField()
    unit = models.FloatField()
    exp_rate = models.FloatField()
    exp_title = models.CharField(max_length=50)
    invoice_inv_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)

class Room(models.Model):
    # room_no = models.AutoField(primary_key=True, verbose_name='room_no', db_column='room_no')
    room_no = models.IntegerField(max_length=10)
    room_rate = models.FloatField()
    status = (

    )
    floor = models.IntegerField(max_length=10)
    dormitory_dorm_id = models.IntegerField(max_length=10)

class Room_contract(models.Model):
    room_room_no = models.ForeignKey(Room, on_delete=models.CASCADE)
    contract_contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)

class Dormitory(models.Model):

    dorm_name = models.CharField(max_length=255)
    dorm_owner = models.CharField(max_length=255)
    dorm_type = (

    )
    open_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    address = models.TextField()
    floor = models.IntegerField(max_length=10)
    phone = models.CharField(max_length=10)

class Facility(models.Model):
    fac_rate = models.FloatField()
    dormitory_dorm_id = models.ForeignKey(Dormitory, on_delete=models.CASCADE)

class Facility_service_type(models.Model):
    facility_fac_id = models.CharField(max_length=5)
    service_types_no = models.IntegerField()

