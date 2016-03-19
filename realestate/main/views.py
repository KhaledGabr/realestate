from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import property

from .forms import PropertyForm

# Create your views here.


# Homepage
def homepage(request):
    return render ( request, "login.html", {} )


# Create
def create(request):
    form = PropertyForm( request.POST or None )    
    context = {
        "form" : form,
    }
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect ( "list")
        return render ( request, "create.html", context )
        
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
def delete(request, id):
    instance = property.objects.get( id=id )
    instance.delete()
    return redirect ( "list")
    
    
