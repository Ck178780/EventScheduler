# Imports:
from datetime import datetime

# Code:

class EventScheduler:
    def __init__(self):
        """
        Initialize an EventScheduler object with an empty list to store events.
        """
        self.events = []

    def add_event(self, event):
        """
        Add a new event to the scheduler.

        Parameters:
        - event (Event): An Event object to be added to the scheduler.

        Returns:
        None
        """
        # Check if the user event title already exists:
        existing_titles = [existing_event.title for existing_event in self.events]
        if event.title in existing_titles:
            print(f"An event with the title '{event.title}' already exists. Cannot add duplicate events.")
        else:
            self.events.append(event)
            print("Event added successfully!")

    def list_events(self):
        """
        Display all events in the scheduler, sorted by date and time.

        Returns:
        None
        """
        sorted_events = sorted(self.events, key=lambda x: x.datetime)
        for event in sorted_events:
            print(str(event))
            
    def search_events(self, query):
        """
        Search for events by date or keyword in the title/description.

        Parameters:
        - query (str): The search query.

        Returns:
        None
        """
        matching_events = []
        for event in self.events:
            if query.lower() in event.title.lower() or query.lower() in event.description.lower() or query == event.date:
                matching_events.append(event)

        if matching_events:
            print("\nMatching Events:")
            for event in matching_events:
                print(str(event))
        else:
            print("No events found that match your search criteria.")
            
    def edit_event(self, title):
        """
        Edit an existing event based on its title.

        Parameters:
        - title (str): Title of the event to be edited.

        Returns:
        None
        """
        # Convert input title to lowercase and strip whitespaces
        input_title = title.lower().strip()

        for event in self.events:
            # Convert existing event title to lowercase and strip whitespaces
            existing_title = event.title.lower().strip()

            if existing_title == input_title:
                print("Current event details:")
                print(str(event))

                new_title = input("Enter new event title (press Enter to keep the current title): ")
                new_description = input("Enter new event description (press Enter to keep the current description): ")

                # Validate new date input
                while True:
                    new_date = input("Enter new event date (YYYY-MM-DD) (press Enter to keep the current date): ")
                    if not new_date:
                        break  # Keep the current date if Enter is pressed
                    try:
                        datetime.strptime(new_date, '%Y-%m-%d')
                        break  # Break the loop if the date is valid
                    except ValueError:
                        print("Oops! Invalid date format. Please use the format 'YYYY-MM-DD'.")

                # Validate new time input
                while True:
                    new_time = input("Enter new event time (HH:MM) (press Enter to keep the current time): ")
                    if not new_time:
                        break  # Keep the current time if Enter is pressed
                    try:
                        datetime.strptime(new_time, '%H:%M')
                        break  # Break the loop if the time is valid
                    except ValueError:
                        print("Oops! Invalid time format. Please use the format 'HH:MM'.")

                # Update event attributes if new values are provided
                if new_title:
                    event.title = new_title
                if new_description:
                    event.description = new_description
                if new_date:
                    event.date = new_date
                    event.datetime = datetime.strptime(f'{event.date} {event.datetime.strftime("%H:%M")}', '%Y-%m-%d %H:%M')
                if new_time:
                    event.datetime = datetime.strptime(f'{event.date} {new_time}', '%Y-%m-%d %H:%M')

                print("Event edited successfully!")
                print("Updated event details:")
                print(str(event))
                return

        print("Event not found.")          
            

    def delete_event(self, title):
        """
        Delete an event from the scheduler based on its title.

        Parameters:
        - title (str): Title of the event to be deleted.

        Returns:
        None
        """
        for event in self.events:
            if event.title == title:
                self.events.remove(event)
                print("Event deleted successfully!")
                return
        print("Event not found.")
        
    def is_title_taken(self, title):
        """
        Check if an event with the given title already exists in the scheduler.

        Parameters:
        - title (str): Title of the event to check.

        Returns:
        bool: True if the title is already taken, False otherwise.
        """
        for event in self.events:
            if event.title == title:
                return True
        return False    