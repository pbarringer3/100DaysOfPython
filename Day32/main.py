import smtplib
from datetime import datetime
import random

now = datetime.now()
day = now.weekday()

if day == 0:
    with open("quotes.txt", 'r') as quotes_file:
        quotes = quotes_file.readlines()
        random_quote = random.choice(quotes)

    with open("credentials.txt", "r") as credentials:
        my_email = credentials.readline().strip()
        password = credentials.readline().strip()
        receiving_email = credentials.readline().strip()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email, 
            to_addrs=receiving_email, 
            msg="Subject:Be Inspired\n\n"+random_quote
        )
        connection.close()