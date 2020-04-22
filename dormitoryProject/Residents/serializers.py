# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from builtins import object
from unittest.util import _MAX_LENGTH

from django.db import models
from rest_framework import serializers

import dormitoryProject

from .models import Contract, Dormitory, Invoice, Resident, Room, Vehicle, Expense, Dormitory, Facility, Facility_service_type

# Create your models here.


# Create your models here.
class ResidentSerializers(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Resident.objects.all())
    fname = serializers.CharField(max_length=100)
    lname = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=10)
    
   
    
class CommentSerializers(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Resident.objects.all())

    name = serializers.CharField(max_length=50)

class ContractSerializers(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Contract.objects.all())
    room_rate = serializers.FloatField()
    start_date = serializers.ReadOnlyField()
    end_date = serializers.ReadOnlyField()
    

    

class VehicleSerializers(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())
    vehicle_type = serializers.CharField(max_length=50) #choice
    vehicle_gen = serializers.CharField(max_length=255)
    

class InvoiceSerializers(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all())
    inv_date = serializers.ReadOnlyField()
    month_no = serializers.IntegerField() #choice
    room_rate = serializers.FloatField()
    water_ex = serializers.FloatField()
    elec_ex = serializers.FloatField()
    
class ExpenseSerializers(serializers.Serializer):
    # exp_no = serializers.IntegerField()
    id = serializers.PrimaryKeyRelatedField(queryset=Expense.objects.all())
    unit = serializers.FloatField()
    exp_rate = serializers.FloatField()
    exp_title = serializers.CharField(max_length=50)

class RoomSerializers(serializers.Serializer):
    # room_no = serializers.IntegerField()
    id = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    room_rate = serializers.FloatField()
   
    floor = serializers.IntegerField()
    dormitory_dorm_id = serializers.IntegerField()

class DormitorySerializers(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Dormitory.objects.all())
    dorm_name = serializers.CharField(max_length=255)
    dorm_owner = serializers.CharField(max_length=255)

    open_time = serializers.ReadOnlyField()
    floor = serializers.IntegerField()
    phone = serializers.CharField(max_length=10)

class FacilitySerializers(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Facility.objects.all())
    fac_rate = serializers.FloatField()

class Facility_service_typeSerializers(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Facility_service_type.objects.all())
    facility_fac_id = serializers.CharField(max_length=5)
    service_types_no = serializers.IntegerField()
