import smtplib

from email.message import EmailMessage


email = EmailMessage()

email['from'] = 'Andrei Neagoie'
email['to'] = 'adderleydex@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'


email.set_content('I am a Python Master!')


with smtplib.SMTP(host='smpt.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()         #connect securly to the server
    
    
    smtp.login('adderleydex@gmail.com', "")
    
    smtp.send_message(email)    
    print('all good boss')
    
    
