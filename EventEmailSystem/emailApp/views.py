from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee, Event
from datetime import datetime

class EmployeeEventData(APIView):

    def get(self, request):
        event_id = request.GET["event_id"]
        current_date = datetime.now()

        if event_id == "1":
            employee_objects = Employee.objects.filter(date_of_birth=current_date).values_list(
                'first_name', 'last_name', 'email_address', 'id',
            )

        else:
            employee_objects = Employee.objects.filter(date_of_joining=current_date).values_list(
                'first_name', 'last_name', 'email_address', 'id',
            )

        try:
            event_data = Event.objects.get(type=event_id)
        except Exception as e:
            return Response("Error in fetching event data")

        
        response = {
            "employee_data_list": employee_objects,
            "template": event_data.template
        }
        
        return Response(response)
