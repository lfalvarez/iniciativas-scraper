from __future__ import print_function

from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime
import os
import json

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = os.getenv('SHEET_ID')

service_account_info = json.loads(os.getenv('SERVICE_ACCOUNT_CREDS'))

credentials = service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)

spreadsheet = service.spreadsheets()

titulo = datetime.today().strftime('%d-%m-%Y:%H')
request_body = {
    'requests': [{
        'addSheet': {
            'properties': {
                'title': titulo,
                'index': 0
            }
        }
    }]
}

add_new_sheet_response = spreadsheet.batchUpdate(
    spreadsheetId=SPREADSHEET_ID,
    body=request_body
).execute()
sheet_id = add_new_sheet_response['replies'][0]['addSheet']['properties']['sheetId']

## agregando el contenido
with open('ordenadas.csv', 'r') as csv_file:
    csvContents = csv_file.read()
subir_contenido_csv_request_body = {
    'requests': [{
        'pasteData': {
            "coordinate": {
                "sheetId": sheet_id,
                "rowIndex": "0",  # adapt this if you need different positioning
                "columnIndex": "0",  # adapt this if you need different positioning
            },
            "data": csvContents,
            "type": 'PASTE_NORMAL',
            "delimiter": ',',
        }
    }, ]}


upload_data_response = spreadsheet.batchUpdate(
    spreadsheetId=SPREADSHEET_ID,
    body=subir_contenido_csv_request_body
).execute()
print(upload_data_response)
