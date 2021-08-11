from django.contrib import admin
from .models import Doctor,Hospital,Event,Report,LoginTime,Appointment,Specialisation , Relationship ,Contact
from .models import User
admin.site.register(User)
admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Event)
admin.site.register(Report)
admin.site.register(LoginTime)
admin.site.register(Appointment)
admin.site.register(Specialisation)
admin.site.register(Relationship)
admin.site.register(Contact)
# Register your models here.
