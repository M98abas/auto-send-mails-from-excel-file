import pandas as pd
import smtplib
import time
'''
Change these to your credentials and name
'''
your_name = "YourName"
your_email = "YourEmail"
your_password = "Your Password"

# If you are using something other than gmail
# then change the 'smtp.gmail.com' and 465 in the line below
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(your_email, your_password)

# Read the file that containe all the mails
email_list = pd.read_excel("data.xlsx")

# Get all the Names, Email Addreses, Subjects and Messages
all_names = email_list['name']
all_emails = email_list['email']

# Loop through the emails
for idx in range(len(all_emails)):

    # Get each records name, email, subject and message
    name = all_names[idx]
    email = all_emails[idx]
    subject = "Hello Auto"
    message = "Hello there {}".format(all_names[idx])

    # Create the email to send
    full_email = ("From: {0} <{1}>\n"
                  "To: {2} <{3}>\n"
                  "Subject: {4}\n\n"
                  "{5}"
                  .format(your_name, your_email, name, email, subject, message))

    # In the email field, you can add multiple other emails if you want
    # all of them to receive the same text
    try:
        server.sendmail(your_email, [email], full_email)
        print('Email to {} successfully sent!\n\n'.format(email))
    except Exception as e:
        print('Email to {} could not be sent :( because {}\n\n'.format(email, str(e)))
    time.sleep(15)
# Close the smtp server
server.close()
