from re import T
from django.db import models

class PropertyManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['property_name'].isalpha()) == False:
            if len(postData['property_name']) < 2:
                errors['property_name'] = "Property name can not be shorter than 2 characters"

        if (postData['owner_name'].isalpha()) == False:
            if len(postData['owner_name']) < 2:
                errors['owner_name'] = "Owner name can not be shorter than 2 characters"

        if (postData['location'].isalpha()) == False:
            if len(postData['location']) < 2:
                errors['location'] = "Location can not be shorter than 2 characters"
        
        if (postData['landmark'].isalpha()) == False:
            if len(postData['landmark']) < 2:
                errors['landmark'] = "Landmark can not be shorter than 2 characters"
        
        if len(postData['pincode']) < 6:
                errors['pincode'] = "Pincode can not be shorter than 6 digits"

        return errors

class Property(models.Model):
    property_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    pincode = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    booked_at = models.DateTimeField(null=True, blank=True, default=None)
    property_type = models.CharField(max_length=255)
    property_status = models.CharField(max_length =100, default="NOT BOOKED")
    buyer = models.CharField(max_length=100, null=True, blank=True, default=None)
    amount = models.IntegerField(null=True, blank=True, default=None)
    objects = PropertyManager()