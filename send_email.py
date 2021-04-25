#Automated script to send emails

import smtplib, ssl, getpass

def send_email(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    To = "to@gmail.com"
    From = "from@gmail.com"
    pw = getpass.getpass(prompt="Password: ", stream=None)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(From, pw)
            server.sendmail(From, To, message)
            print("Email sent!")
        except:
            print("Could not login or send the mail.")
