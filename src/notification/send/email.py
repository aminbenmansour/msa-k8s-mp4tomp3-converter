import smtplib, os, json
from email.message import EmailMessage

def notification(message):
    try:
        message = json.loads(message)
        mp3_fid = message["mp3_fid"]
        sender_address = os.environ["GMAIL_ADDRESS"]
        sender_password = os.environ["GMAIL_PASSWORD"]
        receiver_address = message["username"]

        msg = EmailMessage()
        msg.set_content(f"mp3 file id: {mp3_fid} is now ready!")
        msg["Subject"] = "MP3 Download"
        msg["FROM"] = sender_address
        msg["TO"] = receiver_address

        session = smtplib.SMTP("smtp.gmail.com")
        session.starttls()
        session.login(sender_address, sender_password)
        session.send_message(msg, sender_address, receiver_address)
        session.quit()
        print("Mail sent")

    except:
        pass