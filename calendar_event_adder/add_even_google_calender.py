from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
import os
from pytz import timezone

'''
KEEP IN MIND!!!:
For the first time it runs, it needs to access the google calendar API and to create token.pickle file.
For that you need to make sure that on OAuth consent screen there is test user added (for this time it is ignarvalme@gmail.com)
If previous part is not done, it will throw error. Error 403: access_denied and the token.pickle is not created.

Also you have to make sure that on Credentials page you have OAuth 2.0 client ID and secret added 
and it also has Authorised redirect URIs added (it has to be the same URL you coming form for example http://localhost:8080/).
It will give you Error 400: redirect_uri_mismatch
'''

# get current working directory, NOTE it does not work properly on Linux OS for some reason
working_directory = os.getcwd()
# add event to google calendar


def add_event_to_google_calendar(gmail_address, event_title, event_start_date, event_end_date):

    calendar = GoogleCalendar(credentials_path=f'{working_directory}/calendar_event_adder/credentials.json',
                              calendar=gmail_address)
    event = Event(
        summary=event_title,
        start=event_start_date,
        end=event_end_date,
        # added because of linux timezone error: pytz.exceptions.UnknownTimeZoneError: 'local'
        timezone=str(timezone('Europe/Helsinki')),
        minutes_before_email_reminder=1440  # 24Hrs before
    )

    calendar.add_event(event)