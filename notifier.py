import smtplib
from getAPIdata import *#get all methods
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "fortestingforex@gmail.com"
password = "a0b1c2d3"
send_to_email = "fortestingforex1@gmail.com"

subject = "desired rate detected"
message = ""

msg = MIMEMultipart()
msg["From"] = email
msg["To"] = send_to_email
msg["Subject"] = subject

# forex_data = get_currency_data()
# print(forex_data["USD_CAD"])
# message += "USD is: " + str(forex_data["USD_CAD"]) + " CAD dollars"
# print(message)

# baseAndEx = baseAndEx()
# base = baseAndEx["base"]
# exchange = baseAndEx["exchange"]
base = "USD"
exchange = "CAD"

try:
    (forex_data, formattedKey) = get_currency_data(base + "_" + exchange)
    message += base + " is: " + str(forex_data[formattedKey]) + " " + exchange + " dollars"

    msg.attach(MIMEText(message, "plain"))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
except:
    print("problem retrieving data")

