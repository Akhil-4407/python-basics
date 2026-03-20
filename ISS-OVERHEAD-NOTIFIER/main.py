import requests
from datetime import datetime, timezone, timedelta
import smtplib
import os 
from dotenv import load_dotenv
import time
load_dotenv(".env")
ist_time = timezone(timedelta(hours=5,minutes=30))
MY_LAT =17.385044
MY_LONG =78.486671
def is_close(a,b) -> bool | None:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    time_now = datetime.now().hour
    if (abs(iss_latitude - a) < 5.0) and (abs(iss_longitude - b) < 5.0):
        if time_now >=sunset and time_now<=sunrise:
            return True


parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()





utc_rise_time = data["results"]["sunrise"]
utc_rise_datetime = datetime.fromisoformat(utc_rise_time)
ist_rise_datetime = utc_rise_datetime.astimezone(ist_time)


utc_set_time = data["results"]["sunset"]
utc_set_datetime = datetime.fromisoformat(utc_set_time)
ist_set_datetime = utc_set_datetime.astimezone(ist_time)

sunrise = int(str(ist_rise_datetime).split(" ")[1].split(":")[0])
sunset = int(str(ist_set_datetime).split(" ")[1].split(":")[0])
while True:
    time.sleep(60)
    is_close(MY_LAT,MY_LONG)
    if is_close:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            my_email = os.environ.get("MY_EMAIL")
            my_password = os.environ.get("MY_PASSWORD")
            connection.login(user=my_email,password=my_password)
            connection.sendmail(
                to_addrs="akhil.k.hlc0008@gmail.com",
                from_addr=my_email,
                msg="SUBJECT: ISS Overhead\n\n ISS could be viewed."
            )

        


