# Imports:
from datetime import datetime

# Code:
class Event:
    def __init__(self, title, description, date, time):
        """
        Initialize an Event object with a provided title, description, date, and time.

        Parameters:
        - title (str): Title of the user event.
        - description (str): Description of the user event.
        - date (str): Date of the user event in the format 'YYYY-MM-DD'.
        - time (str): Time of the user event in the format 'HH:MM'.
        """
        try:
            self.datetime = datetime.strptime(f'{date} {time}', '%Y-%m-%d %H:%M')
            self.title = title
            self.description = description
            self.date = date  # Add the date attribute
        except ValueError:
            raise ValueError("Oops! Invalid date or time format. Please run the application again and use YYYY-MM-DD for date and HH:MM for time.")

    def __str__(self):
        """
        Return a string representation of the user event.

        Returns:
        str: String representation of the user event.
        """
        return f"Title: {self.title}\nDescription: {self.description}\nDate: {self.date}\nTime: {self.datetime.strftime('%H:%M')}"