import requests
from datetime import datetime
import smtplib
import time
import secrets

MY_EMAIL = secrets.MY_EMAIL
MY_PASSWORD = secrets.MY_PASSWORD
MY_LAT = 34.052235
MY_LONG = -118.243683

# Return True if your position is within +5/-5 of ISS position


def iss_within_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_lat_upper = latitude + 5
    iss_lat_lower = latitude - 5
    iss_long_upper = longitude + 5
    iss_long_lower = longitude - 5
    if (iss_lat_lower <= MY_LAT <= iss_lat_upper) and (iss_long_lower <= MY_LONG <= iss_long_upper):
        return True
def is_night():
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # Get sunrise and sunset times and get the hours in UTC
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    current_hour = datetime.now().hour
    if sunset_hour <= current_hour <= sunrise_hour:
        return True

# If the ISS is close to my current position and it is currently dark, send email to tell me to look up. Repeats
# every minute


while True:
    time.sleep(60)
    if iss_within_range() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look Up!\n\nThe ISS is above you right now!"
        )


