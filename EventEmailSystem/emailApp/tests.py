from django.test import TestCase, Client
from .models import Employee, Event
from datetime import datetime
from django.urls import reverse
from rest_framework import status


client = Client()

class PuppyTest(TestCase):

    def setUp(self):
        Event.objects.create(
            type='1', template="<html></html>") # for birthday
        
        Employee.objects.create(
            first_name = "first name",
            last_name = "Last name",
            email_address= "test@gml.con",
            date_of_joining = datetime.now(),
            date_of_birth = datetime.now()
        )

    def test_count_of_employee(self):
        employee = Employee.objects.filter(date_of_birth=datetime.now())
        response = client.get(reverse('event_data'), {"event_id": "1"})

        self.assertEqual(
            len(employee), len(response.data['employee_data_list']))
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)