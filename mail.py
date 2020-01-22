import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def Mail(email, name):

    gmail_user = 'visheshsciensism@gmail.com'
    gmail_password = 'ohyeah!!!!'
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = email
    msg['Subject'] = "Review Bay Registration Confirmation"
    body = '''
     Dear {},
        Congratulations, you have successfully registered on review bay. We are expecting a lot of data analysis with you ahead!
        
        
    h3lloworld.py
    '''.format(name)

    body = MIMEText(body)
    msg.attach(body)
    


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, email, msg.as_string())
    server.close()

    print('Email sent!')


Mail('tayalvishesh83@gmail.com', 'Vishesh Tayal')