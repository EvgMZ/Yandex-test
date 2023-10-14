import logging
import os.path

from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

load_dotenv()


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
logging.basicConfig(
    level=logging.ERROR,
    filename='logs.log',
    format="%(asctime)s  %(message)s"
    )
# The ID of a sheets.
DOCUMENT_ID = '1zCaYlpdVLzn7hdgmODPLz7KXom0V-zk_toJ0s7FI4pg'


class GoogleSheets():
    def __init__(self) -> None:
        '''
        auth google drive/sheets
        '''
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        self.service = build('sheets', 'v4', credentials=creds)

    def get_last_rows(self):
        """
        Get last rows
        """
        try:
            data = self.service.spreadsheets().values().get(
                spreadsheetId=DOCUMENT_ID,
                range='A1:E100',
                majorDimension='ROWS'
            ).execute()
            self.last_rows = len(data['values'])
        except Exception as e:
            logging.error(e)

    def add_new_info(self, input_data):
        """
        Add telegram info to google sheets
        """
        try:
            self.result = self.service.spreadsheets().values().batchUpdate(
                spreadsheetId=DOCUMENT_ID,
                body=input_data).execute()
        except Exception as e:
            logging.error(e)
