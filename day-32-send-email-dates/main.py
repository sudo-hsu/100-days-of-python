import smtplib
import secrets
import datetime as dt

# gmail = "test.sudohsu@gmail.com"
# yahoo = "test.sudohsu@yahoo.com"
# gmail_password = secrets.GMAIL_PASSWORD
# yahoo_password = secrets.YAHOO_APP_PASSWORD
# smtp_gmail = "smtp.gmail.com"
# smtp_yahoo = "smtp.mail.yahoo.com"
#
# with smtplib.SMTP(smtp_gmail, port=587) as connection:
#     connection.starttls()
#     connection.login(user=gmail, password=gmail_password)
#     connection.sendmail(from_addr=gmail,
#                         to_addrs=yahoo,
#                         msg="Subject:Hello\n\nThis is the body of the email"
#                         )

anniversary_date = dt.datetime(year=2019, month=4, day=6, hour=16, minute=30)
print(anniversary_date)