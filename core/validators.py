from django.utils import timezone
from django import forms

def present_or_future_date(value): 

    if value < timezone.now(): 
        return False
    return True
