"""
Definition of views.
"""

from datetime import datetime
from sys import exception
# from telnetlib import STATUS
from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
from django.shortcuts import render
from .service.openai_service import get_openai_response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


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
            'title':'Contact Us',
            'message':'',
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
            'title':'About Us',
            'message':'',
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

def infonotprovided(request):
    """Renders the info not found page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/infonotprovided.html',
        {
            'title':"Info Not Provided ",
            'message':'',
            'year':datetime.now().year,
        }
    )

@csrf_exempt 
def openai_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('user_input', '')
            response_text = get_openai_response(user_input)
            return JsonResponse(data=response_text, safe=False)
            # return JsonResponse({"status":"success","message":response_text},status_code=200)  
        except Exception as e:
            print(e);
            return JsonResponse(data=str(e), safe=False)
            # return JsonResponse({"status":"error","message":str(e)},status_code=500)
     #  return render(request, 'openai_form.html')
    return JsonResponse(data="Invalid request", safe=False)
    # return JsonResponse({"status":"error","message":"Invalid request"},status_code=400)