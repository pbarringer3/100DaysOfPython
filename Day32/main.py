import smtplib

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
        msg="Subject:Hello\n\nThis is the body of my email."
    )
    connection.close()