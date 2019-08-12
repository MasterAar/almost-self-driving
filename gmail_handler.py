from __future__ import print_function
from dotenv import load_dotenv
import os
import pickle
import base64
import os.path
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

load_dotenv()
sender = os.getenv('EMAIL_SENDER')
to = os.getenv('EMAIL_TO')


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service


def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string())}


def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(
            userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
    except error:
        print('An error occurred: %s' % error)


api_service = main()

print('sending email now:')

send_message(api_service, sender, create_message(
    sender, to, 'Hi', 'Hello, World!'))
