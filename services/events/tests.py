from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from events.models import Event


class EventsModelTests(TestCase):
    def test_str_repr(self):
        event = Event(name="The Name")
        self.assertTrue(f"{event}" == "The Name")


class EventsIndexViewTests(TestCase):
    def test_no_events(self):
        resp = self.client.get(reverse("events:index"))
        self.assertEqual(resp.status_code, 200)
        self.assertQuerySetEqual(resp.context["latest_events"], [])

    def test_events(self):
        event = Event.objects.create(name="A Name",
                                     start_date=datetime.now(),
                                     end_date=datetime.now(),
                                     location="KRC",
                                     gender="male",
                                     times="ASD",
                                     cost="$300")
        resp = self.client.get(reverse("events:index"))
        self.assertQuerySetEqual(
            resp.context["latest_events"],
            [event],
        )