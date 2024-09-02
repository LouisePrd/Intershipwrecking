from django.contrib import admin
from .models import Application
from .models import Candidate

admin.site.register(Application)
admin.site.register(Candidate)