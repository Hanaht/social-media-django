from django.contrib import admin
from registration.models import Account
from .models import Messages, Friends

# Register your models here.
admin.site.register(Messages)
admin.site.register(Friends)
