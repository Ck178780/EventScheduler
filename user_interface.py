# Imports:
from event_class import Event
from event_scheduler import EventScheduler
from datetime import datetime

# Code:
def get_valid_date():
    """
    Prompt the user for a valid date input in the format 'YYYY-MM-DD'.
    """
    while True:
        date = input("Enter your event date (YYYY-MM-DD): ")
        try:
            # Attempt to convert the input to a valid date
            datetime.strptime(date, '%Y-%m-%d')
            return date
        except ValueError:
            print("Oops!Invalid date format. Please use the format 'YYYY-MM-DD'.")

def get_valid_time():
    """
    Prompt the user for to input a valid time in the format 'HH:MM'.
    """
    while True:
        time = input("Enter your event time (HH:MM): ")
        try:
            # Attempt to convert the input to a valid time
            datetime.strptime(time, '%H:%M')
            return time
        except ValueError:
            print("Oops! Invalid time format. Please use the format 'HH:MM'.")


def main():
    """
    Main function to run the user event scheduler application.
    Manages the user interface and interaction with the EventScheduler class.

    Returns:
    None
    """
    event_scheduler = EventScheduler()

    while True:
        print("\nOptions:")
        print("1. Add Event")
        print("2. List Events")
        print("3. Delete Event")
        print("4. Search Events")
        print("5. Edit Events")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            title = input("Enter your event title: ")
            # Check if the title already exists
            if event_scheduler.is_title_taken(title):
                print(f"An event with the title '{title}' already exists. Cannot add duplicate events.")
                continue
            
            description = input("Enter your event description: ")
            date = get_valid_date()  # Use the validation function for date
            time = get_valid_time()  # Use the validation function for time
            event = Event(title, description, date, time)
            event_scheduler.add_event(event)
        elif choice == '2':
            event_scheduler.list_events()
        elif choice == '3':
            title = input("Enter the title of the event to delete: ")
            event_scheduler.delete_event(title)
        elif choice == '4':
            search_query = input("Enter search query (date, title, or keyword): ")
            event_scheduler.search_events(search_query)
        elif choice == '5':
            title = input("Enter the title of the event to edit: ")
            event_scheduler.edit_event(title)    
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
    