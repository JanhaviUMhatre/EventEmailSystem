from django.urls import path
from .views import EmployeeEventData

urlpatterns = [
    path('event-data', EmployeeEventData.as_view(), name="event_data"),
]