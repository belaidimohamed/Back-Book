from django.contrib import admin
from .models import UserProfile , Friends , Messages , Forum , Groupp 
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Friends)
admin.site.register(Messages)
admin.site.register(Forum)
admin.site.register(Groupp)