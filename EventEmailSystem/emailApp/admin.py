from django.contrib import admin
from .models import (
    Employee, Event, EventData, EventLog
)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(EventData)
class EventDataAdmin(admin.ModelAdmin):
    pass

@admin.register(EventLog)
class EventLogAdmin(admin.ModelAdmin):
    pass