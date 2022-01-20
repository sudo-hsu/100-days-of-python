import smtplib
import secrets
import datetime as dt
import random

gmail = "test.sudohsu@gmail.com"
yahoo = "test.sudohsu@yahoo.com"
gmail_password = secrets.GMAIL_PASSWORD
#yahoo_password = secrets.YAHOO_APP_PASSWORD
smtp_gmail = "smtp.gmail.com"
#smtp_yahoo = "smtp.mail.yahoo.com"

current_dt = dt.datetime.now()
day_of_week = current_dt.weekday()

with open("quotes.txt", "r") as data:
    quotes_list = data.read().splitlines()

# If it's a Monday, grab a random inspirational quote.
if day_of_week == 0:
    random_quote = random.choice(quotes_list)
    with smtplib.SMTP(smtp_gmail, port=587) as connection:
        connection.starttls()
        connection.login(user=gmail, password=gmail_password)
        connection.sendmail(from_addr=gmail,
                            to_addrs=yahoo,
                            msg=f"Subject:Time for your inspirational Monday quote!\n\n{random_quote}"
                            )



