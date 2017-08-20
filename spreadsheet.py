import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

client = gspread.authorize(creds)
sheet = client.open('neu').sheet1
print(sheet.get_all_records())

# row = ["I'm", "updating", "a", "spreadsheet", "from", "python"]
# index = 1
# # sheet.delete_row(3)
# sheet.update_row(row, index)
# #
