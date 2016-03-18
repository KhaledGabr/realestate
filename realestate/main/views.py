from django.http import HttpResponse
from django.shortcuts import render

from .models import property

from .forms import PropertyForm

# Create your views here.


# Homepage
def homepage(request):
    return render ( request, "login.html", {} )


# Create
def create(request):
    form = PropertyForm( request.POST or None )
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    
    
    
    context = {
        "form" : form,
    }
    return render ( request, "create.html", context )
    
# READ
def list(request):
    queryset = property.objects.all()
    context = {
        "properties" : queryset
    }
    return render (request, "list.html", context)
    
def detail(request, id):
    
    singleproperty = property.objects.get( id=id )
    context = {
        "property" : singleproperty
    }
    return render (request, "detail_api.html", context)
    
    

# Update
def update(request):
    return HttpResponse( "update")

# Delete
def delete(request):
    return HttpResponse( "delete")
    
    
