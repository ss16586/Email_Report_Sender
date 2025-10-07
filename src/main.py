import smtplib      # is used to send the email via an SMTP server.
from email.mime.multipart import MIMEMultipart   # create email structure 
from email.mime.application import MIMEApplication # PDF 
from email.mime.text import MIMEText     # create the text content 
import dotenv
import os
import schedule
import time
dotenv.load_dotenv()
def send_mail():
    # Email configuration 
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = "shubhamsahu346@gmail.com"
    receiver_email = "shubham.d.sahu@capgemini.com"
    password = os.getenv('password')


    # Create the email content 

    msg = MIMEMultipart()
    msg['from'] = sender_email
    msg['to'] = receiver_email
    msg['subject'] = 'Testing Daily report'

    body = "Hello All,\nPlease find the daily report for testing data.\n--\nThanks & Regards,\nShubham."
    msg.attach(MIMEText(body, 'plain'))

    filename = 'C:/Project/Email_Report_Sender/reports/Test_case_daily_results.csv'
    with open(filename, 'rb') as f:
        pdf_attachment = MIMEApplication(f.read(), _subtype='csv')
        pdf_attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(pdf_attachment)


    try:
        server = smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()

        #login to the email account 
        server.login(sender_email,password)

        # send the email 
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # terminate the session 

        server.quit()

        print("Email Sent Successfully")

    except Exception as e:
        print(f' Faild to send email: {e}')

schedule.every().day.at("00:54").do(send_mail)

while True:
    print("Running schedule Task... ")
    schedule.run_pending()
    time.sleep(60)







