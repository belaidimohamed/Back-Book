from django.contrib import admin
from .models import UserProfile , Friends , Messages 
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Friends)
admin.site.register(Messages)