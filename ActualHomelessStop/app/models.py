"""
Definition of models.
"""
#appname/models.py

from django.db import models

class Nonprofit(models.Model):
    # Define fields for the Donor model
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(unique=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    donation_link = models.CharField(max_length=100, blank=True, null=True)
    volunteer_link = models.CharField(max_length=100, blank=True, null=True)
    newspaper_signup = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # String representation of the Donor model

    def __str__(self):
        return f"{self.name}"




