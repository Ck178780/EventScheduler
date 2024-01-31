# Imports:
import unittest
from datetime import datetime
from event_scheduler import EventScheduler
from event_class import Event

# Code:
class TestEventScheduler(unittest.TestCase):
    def setUp(self):
        self.event_scheduler = EventScheduler()

    def test_add_event(self):
        event = Event("Test Event", "Description", "2024-02-01", "14:00")
        self.event_scheduler.add_event(event)
        self.assertIn(event, self.event_scheduler.events)

    def test_delete_event(self):
        event = Event("Test Event", "Description", "2024-02-01", "14:00")
        self.event_scheduler.events.append(event)
        self.event_scheduler.delete_event("Test Event")
        self.assertNotIn(event, self.event_scheduler.events)

    def test_edit_event(self):
        event = Event("Test Event", "Description", "2024-02-01", "14:00")
        self.event_scheduler.events.append(event)
        new_title = "Updated Test Event"
        self.event_scheduler.edit_event("Test Event")
        self.assertEqual(event.title, new_title)

    def test_search_events(self):
        event1 = Event("Event 1", "Description", "2024-02-01", "14:00")
        event2 = Event("Event 2", "Description", "2024-02-02", "15:00")
        self.event_scheduler.events = [event1, event2]

        # Test searching by title
        result = self.event_scheduler.search_events("Event 1")
        self.assertIn(event1, result)
        self.assertNotIn(event2, result)

        # Test searching by date
        result = self.event_scheduler.search_events("2024-02-02")
        self.assertIn(event2, result)
        self.assertNotIn(event1, result)

if __name__ == '__main__':
    unittest.main()