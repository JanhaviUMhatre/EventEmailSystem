from django.db import models
from datetime import datetime
from .constants import EVENT_CHOICES

class Employee(models.Model):
    """
    employee data with basic details
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    date_of_joining = models.DateField(blank=True)
    date_of_birth = models.DateField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_employee_name(self):
        return self.first_name + " " + self.last_name



class Event(models.Model):
    """
    events - birthday / work anniversary 
    can add more events 
    every event will have unique id
    """
    id = models.AutoField(primary_key=True)
    type = models.CharField(choices=EVENT_CHOICES, default="1", max_length=255)
    template = models.TextField()

    def __str__(self):
        return self.type



class EventLog(models.Model):
    """
    new row will be added once cron send email will execute
    description will be updated when there is no data for current date
    success will set to false if cron fails to send email
    acccordingly error and employee array will get updated
    employee array will have id of employee for which process failed
    """
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    error = models.TextField(null=True, default="[]")
    employee_array = models.TextField(null=True, default="[]")
    description = models.CharField(max_length=255, null=True)
    success = models.BooleanField(default=True)



class EventData(models.Model):
    """
    entry for every email sent for employee
    """
    id = models.AutoField(primary_key=True)
    employee_object = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE)
    event_type = models.CharField(choices=EVENT_CHOICES, max_length=255)
    event_log_object = models.ForeignKey(EventLog, null=True, on_delete=models.SET_NULL)
    mail_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee_object.email_address
