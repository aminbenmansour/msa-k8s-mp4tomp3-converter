import smtplib, os, json
from email.message import EmailMessage

def notification(message):
    try:
        message = json.loads(message)
        mp3_fid = message["mp3_fid"]
        sender_address = os.environ["GMAIL_ADDRESS"]
        sender_password = os.environ["GMAIL_PASSWORD"]
        receiver_address = message["username"]

    except:
        pass