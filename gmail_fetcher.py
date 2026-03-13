import imaplib
import email

def fetch_job_emails():

    EMAIL = "yourgmail@gmail.com"
    PASSWORD = "your_app_password"

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, PASSWORD)

    mail.select("inbox")

    status, messages = mail.search(None, '(FROM "linkedin")')

    email_ids = messages[0].split()

    jobs = []

    for e_id in email_ids:

        status, msg_data = mail.fetch(e_id, "(RFC822)")
        raw_email = msg_data[0][1]

        msg = email.message_from_bytes(raw_email)

        subject = msg["subject"]

        jobs.append(subject)

    return jobs