from django.contrib import admin
from .models import Nonprofit
from .models import Event

admin.site.register(Nonprofit)
admin.site.register(Event)