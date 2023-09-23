import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = ['https://www.googleapis.com/auth/photoslibrary.readonly']


def main():
  creds = None
  if os.path.exists('creds/token.json'):
    creds = Credentials.from_authorized_user_file('creds/token.json', SCOPES)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file('creds/credentials.json', SCOPES)
      creds = flow.run_local_server(port=5500)
      with open('creds/token.json', 'w') as token:
            token.write(creds.to_json())


if __name__ == '__main__':
  main()
