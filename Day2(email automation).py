import os
import smtplib
from email.mime.text import MIMEText
from pathlib import Path

import gspread
from google.oauth2.service_account import Credentials

# Google Sheets authentication
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

BASE_DIR = Path(__file__).resolve().parent
CREDENTIALS_PATH = BASE_DIR / "credentials.json"

if not CREDENTIALS_PATH.exists():
    raise FileNotFoundError(f"Credentials file not found: {CREDENTIALS_PATH}")

credentials = Credentials.from_service_account_file(str(CREDENTIALS_PATH), scopes=SCOPES)
client = gspread.authorize(credentials)

# Open Google Sheet
sheet = client.open("Google Form Responses").sheet1

headers = sheet.row_values(1)
required_columns = ["Name", "Email", "Message"]
missing_columns = [col for col in required_columns if col not in headers]

if missing_columns:
    raise ValueError(f"Missing required columns in the sheet: {missing_columns}")

if "Status" not in headers:
    status_col = len(headers) + 1
    sheet.update_cell(1, status_col, "Status")
    headers = sheet.row_values(1)

status_col = headers.index("Status") + 1
rows = sheet.get_all_values()[1:]

# Gmail details
SENDER = os.getenv("SENDER_EMAIL", "your_email@gmail.com")
APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD", "your_app_password")

for row_index, values in enumerate(rows, start=2):
    row = dict(zip(headers, values))
    name = (row.get("Name") or "").strip()
    receiver = (row.get("Email") or "").strip()
    message = row.get("Message") or ""
    status = (row.get("Status") or "").strip().lower()

    if not name or not receiver:
        continue

    if status == "sent":
        continue

    email_body = f"""
Hello {name},

{message}

This email was automatically generated from your Google Form submission.

Regards,
Your Team
"""

    msg = MIMEText(email_body)
    msg["Subject"] = "Response Received"
    msg["From"] = SENDER
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER, APP_PASSWORD)
            server.sendmail(SENDER, receiver, msg.as_string())

        sheet.update_cell(row_index, status_col, "Sent")
        print(f"Email sent to {receiver}")

    except Exception as e:
        sheet.update_cell(row_index, status_col, "Failed")
        print(f"Failed to send email to {receiver}: {e}")
