from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Property

from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'properties.html')

def showPropertyForm(request):
    return render(request, 'propertyForm.html')

def addProprty(request):
    errors = Property.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/properties/add_property')
    property = Property.objects.create(
        property_name=request.POST['property_name'],
        owner_name = request.POST['owner_name'],
        location = request.POST['location'],
        landmark = request.POST['landmark'],
        pincode = request.POST['pincode'],
        property_type = request.POST['property_type']
        )
    property.save()
    return redirect('/properties')

def showPropertyDashboard(request):
    properties = Property.objects.all()
    return render(request, 'propertyDashboard.html', {
        'properties': properties,
    })

def showProperties(request):
    properties = Property.objects.filter(property_status = 'NOT BOOKED')
    return render(request, 'displayProperties.html', {
        'properties': properties,
    })

def bookedDashboard(request):
    properties = Property.objects.filter(property_status = 'BOOKED')
    return render(request, 'boookedDashboard.html', {
        'properties': properties,
    })


def bookProperty(request, id):
    property = Property.objects.get(id=id)
    return render(request, 'bookProperty.html', {
        'property': property,
    })


def buyProperty(request, id):
    amount = request.POST['amount']
    name = request.POST['name']
    property = Property.objects.get(id=id)
    property.amount = amount
    property.buyer = name
    property.booked_at = datetime.now()
    property.property_status = "BOOKED"
    property.save()
    return render(request, 'feedback.html')