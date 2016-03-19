from django import forms
from .models import property



# Reference: Try Django 1.9 - 20 of 38 - Model Form & Create View 

class PropertyForm( forms.ModelForm ):
    class Meta:
        model = property
        fields = [
            "property_title",
            "property_description",
            "property_address",
            "property_price",
            "property_owner_name",
            "property_owner_phone",
        ]
        
        
# this is copied from http://stackoverflow.com/questions/5827590/css-styling-in-django-forms    
    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        self.fields['property_title'].widget.attrs.update({'class' : 'myfieldclass'})
        self.fields['property_description'].widget.attrs.update({'class' : 'myfieldclass'})
        self.fields['property_address'].widget.attrs.update({'class' : 'myfieldclass'})
        self.fields['property_price'].widget.attrs.update({'class' : 'myfieldclass'})
        self.fields['property_owner_name'].widget.attrs.update({'class' : 'myfieldclass'})
        self.fields['property_owner_phone'].widget.attrs.update({'class' : 'myfieldclass'})