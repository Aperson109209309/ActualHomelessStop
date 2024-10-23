"""
Definition of urls for ActualHomelessStop.
"""

from datetime import datetime
# from _pytest.monkeypatch import K
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf import settings
from django.conf.urls.static import static
from app.views import openai_view

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('nonprofitlist', views.nonprofitlist, name='nonprofitlist'),
    path('nonprofitdetails/<int:id>', views.nonprofitdetails, name='nonprofitdetails'),
    path('login',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log In',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('nonprofitdetails/infonotprovided', views.infonotprovided, name='infonotprovided'),
    path('openai/', views.openai_view, name='openai_view')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
