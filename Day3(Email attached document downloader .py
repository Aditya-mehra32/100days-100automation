import imaplib
import email
import os

# ---------------- SETTINGS ----------------
EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_16_digit_app_password"

DOWNLOAD_FOLDER = "email_attachments"

# Create folder if it doesn't exist
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# ---------------- CONNECT TO GMAIL ----------------
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, APP_PASSWORD)

mail.select("inbox")

# Search unread emails
status, messages = mail.search(None, "UNSEEN")

email_ids = messages[0].split()

print(f"Found {len(email_ids)} unread emails.")

# ---------------- DOWNLOAD ATTACHMENTS ----------------
for email_id in email_ids:

    status, data = mail.fetch(email_id, "(RFC822)")

    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)

    print("\nFrom:", msg["From"])
    print("Subject:", msg["Subject"])

    # Check every part of the email
    for part in msg.walk():

        # Get filename
        filename = part.get_filename()

        if filename:

            filepath = os.path.join(
                DOWNLOAD_FOLDER,
                filename
            )

            # Save attachment
            with open(filepath, "wb") as file:
                file.write(part.get_payload(decode=True))

            print("Downloaded:", filename)

# ---------------- CLOSE CONNECTION ----------------
mail.close()
mail.logout()

print("\n✅ All attachments downloaded successfully!")
