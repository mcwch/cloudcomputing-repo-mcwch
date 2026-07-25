# Module 10 Flask Logging Lab

This lab demonstrates basic application logging in Flask.

The application uses Python's built-in logging module. Accessing the home page creates an INFO log, while accessing the /error route creates an ERROR log. Each log includes a timestamp, log level, and message. These logs help developers track application activity and troubleshoot problems.

## Routes

- / records an INFO log and displays the home page.
- /error records a simulated ERROR log.

## Run

python app.py
