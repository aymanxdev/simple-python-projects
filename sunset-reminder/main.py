import requests
import datetime as dt
import time
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

my_email = "Your sender email"
my_password = "Your password"
to_address = "receiving email address"

def check_if_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response =requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    today_time = dt.datetime.now()
    hour = today_time.hour

    if hour >= sunset or hour <= sunrise:
        return True


if check_if_overhead() and is_night():
  connection = smtplib.SMTP("smtp.gmail.com")
  connection.starttls()
  connection.login(user=my_email, password=my_password)
  connection.sendmail(to_addrs=to_address, msg='Subject: Look up 🙋‍♀️\n\n It is above you in the sky')


print("code is working")
