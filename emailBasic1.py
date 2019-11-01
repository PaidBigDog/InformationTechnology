import smtplib
from time import 

email = 'goodshepherdiot@gmail.com' # your email
password = 'P@ssword#1' # your email password
send_to_email = 'busterplummer@gmail.com' # who we are sending the message to
message = 'Michael is doe XD XD XD XD'  # the message in the email

while True:
    server = smtplib.SMTP('smtp.gmail.com', 587) # connect to the server
    server.starttls() # use TLS (Transport Layer Security)
    server.login(email, password)
    server.sendmail(email, sent_to_email, message)
    sleep(10)

server.quit()