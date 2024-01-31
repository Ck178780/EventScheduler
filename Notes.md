Own notes:
Is there a software pattern I can apply?
    No --> This is a simple application and straightforward which doesn't really justify the use of complex software patterns, however I can apply the principle of Seperation of Concern, improve the maintainability & extensibility. Divide the program into three files "event_class", "event_scheduler" and "user_interface"

Generate docstrings for every function, must be clear, concise and precise
   Yes -> All applicable docstrings are inserted.

What if a user types the date or time in a wrong format?
Use real-time input validation loops to ensure the user enters the correct date and time formats before moving on to the next input. Ensuring that the progarm/application does not exit if an error occurs.

Also added a feature that prevents a user from entering an event which already exists.



   