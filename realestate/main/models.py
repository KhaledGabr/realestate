from __future__ import unicode_literals
from django.db import models

class property (models.Model):
    #property_uploader = models.ForeignKey(User)
    
    property_title = models.CharField( max_length = 200 )
    property_description = models.TextField( max_length = 1000 )
    property_address = models.CharField( max_length = 300 )
    property_price = models.IntegerField ()
    property_owner_name = models.CharField( max_length = 200 )
    property_owner_phone = models.CharField( max_length = 30 )
    property_owner_comments = models.CharField( max_length = 200 )
    
    date_updated = models.DateTimeField( auto_now = True, auto_now_add=False)
    date_created = models.DateTimeField(auto_now = False, auto_now_add=True)

    def __str__(self):
        return self.property_title

