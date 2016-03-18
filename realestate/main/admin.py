from django.contrib import admin

from .models import property

class PostModelAdmin(admin.ModelAdmin):
    list_display = [ "property_title", "property_owner_name"]
    class Meta:
        model = property

admin.site.register(property, PostModelAdmin)