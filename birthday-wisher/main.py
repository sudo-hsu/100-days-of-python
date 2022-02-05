import datetime as dt
import pandas
import random
import smtplib
import secrets

gmail = secrets.GMAIL
gmail_password = secrets.GMAIL_PASSWORD
smtp_gmail = "smtp.gmail.com"

current_dt = dt.date.today()
today = (current_dt.month, current_dt.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()
}
if today in birthdays_dict:
    birthday_pal = birthdays_dict[today]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", birthday_pal["name"])
    with smtplib.SMTP(smtp_gmail, port=587) as connection:
        connection.starttls()
        connection.login(user=gmail, password=gmail_password)
        connection.sendmail(from_addr=gmail,
                            to_addrs=birthday_pal["email"],
                            msg=f"Subject: Happy Birthday!\n\n{letter}"
                            )




