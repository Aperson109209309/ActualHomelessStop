"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
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

def nonprofitdetails(request):
    """Renders the nonprofit details page."""
    assert isinstance(request, HttpRequest)
    nonprofits = Nonprofit.objects.all()
    return render(
        request,
        'app/about.html',
        {
            'title':'Nonprofit Details (CHANGE TO NONPROFIT NAME)',
            'message':'Your application description page. (CHANGE TO NONPROFIT DESCRIPTION OR SMTH ELSE',
            'year':datetime.now().year,
        }
    )
