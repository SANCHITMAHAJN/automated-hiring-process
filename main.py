#Hiring Script for Automation Assistant role


# Importing libraries

import pandas as pd						
import numpy as np
import csv
from email.message import EmailMessage
import ssl
import smtplib


# Read CSV
df = pd.read_csv('candidates.csv')


# Filter Candidates based on criteria
selected_candidates = df[(df['Automation_Exp'] == 'Yes') & (df['Availability'] == 'PT') & (df['IT_Experience'] == 'Yes')]


# Create a new sheet with selected candidates list
selected_candidates.to_csv('Selected.csv')
df = pd.read_csv('Selected.csv')

# Create an email list from the Selected candidates list
email_list = df['Email'].tolist()
# print(email_list)

#open selected.csv file
with open('Selected.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)      				#Skipping 1st line (ID/Email tags)


    for line in reader:
        text = "Hello " + line[2] + ", \n Congrats, you have been selected for an interview for the Automation 			Assistant role. \n Please let us know what time during office hours on Wednesday works for you. \n \n  		Best, \n HR Team"

        email_receiver = line[9]
        email_sender = 'hr@xyzcorp.com'
        email_password = '###########'

        subject = "Automation Assistant Interview"
        body = text

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        # for security

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

