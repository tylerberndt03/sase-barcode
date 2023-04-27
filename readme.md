You have to connect your Google Account (the SASE Google account, with member sheets etc.) to gspread.

Navigate here: https://console.cloud.google.com/ and follow these steps.

1. Create a new project.

2. Open the sidebar, open APIs and Services, and click "+ Enable APIs and Services".

3. Search for and enable "Google Drive API" and "Google Sheets API".

4. Go to Credentials, select "Create crdentials -> Service account", and fill the form out. The (optional) parts can be ignored for now.

5. On the Credentials screen, select "Manage service accounts".

6. Click the three dots next to the servoce account you just made, go to "Manage keys -> Add key -> Create new key" and select a JSON key.

7. You just downloaded a file. Go to %APPDATA%/gspread (make this directory if it doesn't exist) and rename it service_account.json.

To make this script work, there needs to be a "Members" spreadsheet containing member info for SASE members, with the UFID in the first column. This spreadsheet and the target spreadsheet have to be connected to the service account; find the email on the Credentials page and share the spreadsheet with that email as you would any other.

When the script starts, type in the name of the target spreadsheet.
