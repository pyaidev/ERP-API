from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Event


class EventAPITestCase(APITestCase):
    def setUp(self):
        # Create a sample Event object for testing
        self.event = Event.objects.create(
            title="Test Event",
            description="This is a test event",
            slug="test-event",
            address="1234 Test St",
            start_date="2023-04-15T10:00:00Z",
            end_date="2023-04-15T12:00:00Z",
            is_active=True

        )

    def test_event_list_api_view(self):
        url = reverse('event:event-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_create_api_view(self):
        url = reverse('event:event-create')
        data = {
            'title': 'New Event',
            'description': 'This is a new event',
            'slug': 'new-event',
            'address': '5678 New St',
            'start_date': '2023-04-15T14:00:00Z',
            'end_date': '2023-04-15T16:00:00Z',
            'is_active': True
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 2)  # Check that a new Event object was created

    def test_event_delete_api_view(self):
        url = reverse('event:event-delete', args=[self.event.slug])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Event.objects.count(), 0)  # Check that the Event object was deleted

    def test_event_detail_api_view(self):
        url = reverse('event:event-detail', args=[self.event.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'],
                         self.event.title)  # Check that the returned data matches the Event object

    def test_event_update_api_view(self):
        url = reverse('event:event-update', args=[self.event.slug])
        data = {
            'title': 'Updated Event',
            'description': 'This is an updated event',
            'address': '5678 Updated St',
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.event.refresh_from_db()
        self.assertEqual(self.event.title, 'Updated Event')  # Check that the Event object was updated
