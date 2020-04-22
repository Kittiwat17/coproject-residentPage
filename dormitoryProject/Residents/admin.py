# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Resident, Comment, Contract, Vehicle, Invoice, Expense, Room, Room_contract, Dormitory, Facility, Facility_service_type

# Register your models here.
admin.site.register(Resident)

admin.site.register(Comment)

admin.site.register(Contract)

admin.site.register(Vehicle)

admin.site.register(Invoice)

admin.site.register(Expense)

admin.site.register(Room)

admin.site.register(Room_contract)

admin.site.register(Dormitory)

admin.site.register(Facility)

admin.site.register(Facility_service_type)




