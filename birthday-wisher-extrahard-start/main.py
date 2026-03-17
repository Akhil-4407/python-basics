##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas as pd
import random
data = pd.read_csv("./birthdays.csv")

def call(to_email,name):
    my_email= "akhilkosuri44@gmail.com"
    my_password = "wpmz zjvu clcd dhnp"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt","r") as file:
            data = file.readlines()
        data[0] = data[0].replace("[NAME]",name)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg="Subject: Happy Birthday\n\n" + "".join(data)

        )
now = dt.datetime.now()
current_day = now.day
current_month = now.month
data = data.to_dict(orient="records")
print(data)
for i in data:
    if current_day == i["day"] and current_month == i["month"]:
        call(i["email"],i["name"])
