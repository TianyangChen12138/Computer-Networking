import smtplib

import config

msg = "I love computer networks!"

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(config.EMAIL_ADDRESS, config.PASSWORD)
message = '{}'.format(msg)
server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
print("Success: Email sent!")
server.quit()
print("Success: Quit!")
