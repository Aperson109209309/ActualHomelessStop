"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest

from app.models import Nonprofit

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def nonprofitlist(request):
    """Renders the nonprofit list page."""
    assert isinstance(request, HttpRequest)
    nonprofits = Nonprofit.objects.all()
    return render(
        request,
        'app/nonprofitlist.html',
        {
            'title':'Nonprofit List',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'nonprofits':nonprofits,
        }
    )

def nonprofitdetails(request, id):
    """Renders the nonprofit details page."""
    assert isinstance(request, HttpRequest)
    # nonprofits = Nonprofit.objects.all()
    object = get_object_or_404(Nonprofit,id = id)
    return render(
        request,
        'app/nonprofitdetails.html',
        {
            'title':'Nonprofit Details (CHANGE TO NONPROFIT NAME)',
            'message':'Your application description page. (CHANGE TO NONPROFIT CATEGORY',
            'year':datetime.now().year,
            'object': object 
        }
    )
