import streamlit as st
import imaplib
import email
import schedule, time
from crontab import CronTab




def read_mails():
    st.title("Email Reader")
    host='imap.gmail.com'
    username='rajinder@swissbeauty.in'
    password='9711609399A'

    mail=imaplib.IMAP4_SSL(host)
    mail.login(username,password)
    mail.select('INBOX')

    _,search_data=mail.search(None,'(FROM "supply@meesho.com")','(FROM "supply@meesho.com")',"UNSEEN")


    for i in search_data[0].split():
        _,data=mail.fetch(i,'(RFC822)')
        email_body=data[0][1]
    #     # print(email_body)
        email_body=email.message_from_bytes(email_body)
        # if email_body['From']=='supply@meesho.com':
        #     print('From:',email_body['From'])
        #     print('Subject:',email_body['Subject'])
        #     print('Body:',email_body.get_payload())
            # mail.store(i,'+FLAGS','\Seen')


if __name__=='__main__':
    read_mails()