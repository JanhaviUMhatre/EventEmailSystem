import requests
from django.conf import settings
import json
from django.utils.html import strip_tags
from .models import EventData, EventLog, Employee
from .mailer import send_mail
from .constants import EVENT_CHOICES
from datetime import datetime

BASE_URL = settings.BASE_URL
EVENT_CHOICES_DICT = dict(EVENT_CHOICES) 


def send_event_email(event_id):
    params = {"event_id": event_id}
    event = EVENT_CHOICES_DICT[event_id]
    try:
        response = requests.get(BASE_URL+'/event-data', params=params)
    except Exception as e:
        return
    
    response = json.loads(response.text)
    event_log_object = EventLog.objects.create(timestamp=datetime.now())
    event_log_object.error = []
    event_log_object.employee_array = []
    event_data_objects_array = []

    if not response['employee_data_list']:
        event_log_object.description = f"No records Found : {event}"
        event_log_object.save()
        return
    for employee_data in response['employee_data_list']:
        try:
            employee = Employee.objects.get(id=int(employee_data[3]))
        except Exception as e:
            event_log_object.error.append(e)
            continue
        name = employee_data[0] + " " + employee_data[1]
        template = response["template"].format(name=name.title())
        plain_message = strip_tags(template)
        subject = "Happy Birthday!"
        if event_id == "2":
            subject = "Happy Work Anniversary!"
        try:
            send_mail(plain_message, employee_data[2], subject)
            event_data_object = EventData(
                employee_object=employee, event_type=event_id, 
                event_log_object=event_log_object, mail_time= datetime.now()
            )
            event_data_objects_array.append(event_data_object)
        except Exception as e:
            event_log_object.error.append(e)
            event_log_object.employee_array.append(employee_data[3])
            event_log_object.success = False
        
        
    try:
        EventData.objects.bulk_create(event_data_objects_array)
    except Exception as e:
        event_log_object.error.append(e)
    event_log_object.save()
