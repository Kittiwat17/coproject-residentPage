# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from fnmatch import filter
from tkinter.tix import Select

from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.renderers import JSONRenderer

from .models import Contract, Invoice, Resident, Room, Room_contract
from .serializers import ContractSerializers, InvoiceSerializers


def residents_page(request):
    resident = Resident.objects.get(pk=1)
    contracts = Contract.objects.filter(resident_resident_id=resident)
 
    roomOfResident = []
    for contract in contracts:
        roomOfResident.append(Room_contract.objects.filter(contract_contract_id=contract))

    return render(request, template_name='Residents-Page.html', context={
        'Resident': resident,
        'Contracts': contracts,
        'Rooms': roomOfResident,
    })
# Create your views here.

def CheckCost(request):
    # data = json.loads(request.body)
# JSONparser().parse()
    resident = Resident.objects.get(pk=1)
    residentContract = Contract.objects.filter(resident_resident_id=resident)
    # itemset_list_ids = [Contract for itemset in residentContract]
    # inv_id = []
    # for contract in residentContract:
    #     inv_id.append(Invoice.objects.filter(contract_contract_id=contract))
    
    # invoiceList = []
    invoiceDict = {}

    # เก็บใบแจ้งนี้ทั้งหมด ของสัญาทั้งหมดที่ทำไว้
    i = 0
    for contract in residentContract:
        invoices = Invoice.objects.filter(contract_contract_id=contract)
        invoiceSerializerCell = InvoiceSerializers(invoices, many=True)
        invoiceDict[i] = invoiceSerializerCell.data
        # invoiceList.append(invoiceDict)
        i = i+1
    #
    
    
    # contractSerializer = ContractSerializers(residentContract, many=True)

    # content = JSONRenderer().render(contractSerializer.data)

    return JsonResponse(invoiceDict,status=200, safe=False)
