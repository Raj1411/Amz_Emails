import streamlit as st
import imaplib
import email
import schedule, time
# from crontab import CronTab


st.title("Email Reader")

btn=st.button('Read Amz Mails')

def read_mails():
    if btn:
        host='imap.gmail.com'
        username='srajinder816@gmail.com'
        password=st.secrets['KEY']

        mail=imaplib.IMAP4_SSL(host)
        mail.login(username,password)
        mail.select('INBOX')

        _,search_data=mail.search(None,'(FROM "do-not-reply@amazon.in")','(FROM "do-not-reply@amazon.in")',"UNSEEN")


        for i in search_data[0].split():
            _,data=mail.fetch(i,'(RFC822)')
            email_body=data[0][1]
            email_body=email.message_from_bytes(email_body)
            
            
            
def read_mails_1():
    if btn:
        host='imap.gmail.com'
        username='srajinder816@gmail.com'
        password=st.secrets['KEY']

        mail=imaplib.IMAP4_SSL(host)
        mail.login(username,password)
        mail.select('INBOX')

        _,search_data=mail.search(None,'(FROM "donotreply@amazon.com")','(FROM "donotreply@amazon.com")',"UNSEEN")


        for i in search_data[0].split():
            _,data=mail.fetch(i,'(RFC822)')
            email_body=data[0][1]
            email_body=email.message_from_bytes(email_body)
            
            
            

 
def read_mails_2():
    if btn:
        host='imap.gmail.com'
        username='srajinder816@gmail.com'
        password=st.secrets['KEY']

        mail=imaplib.IMAP4_SSL(host)
        mail.login(username,password)
        mail.select('INBOX')

        _,search_data=mail.search(None,'(FROM "order-update@amazon.com")','(FROM "order-update@amazon.com")',"UNSEEN")


        for i in search_data[0].split():
            _,data=mail.fetch(i,'(RFC822)')
            email_body=data[0][1]
            email_body=email.message_from_bytes(email_body)
            
            
            
            

def read_mails_3():
    if btn:
        host='imap.gmail.com'
        username='srajinder816@gmail.com'
        password=st.secrets['KEY']

        mail=imaplib.IMAP4_SSL(host)
        mail.login(username,password)
        mail.select('INBOX')

        _,search_data=mail.search(None,'(FROM "seller-answers@amazon.in")','(FROM "seller-answers@amazon.in")',"UNSEEN")


        for i in search_data[0].split():
            _,data=mail.fetch(i,'(RFC822)')
            email_body=data[0][1]
            email_body=email.message_from_bytes(email_body)
            
            
            
            
 
def read_mails_4():
    if btn:
        host='imap.gmail.com'
        username='srajinder816@gmail.com'
        password=st.secrets['KEY']

        mail=imaplib.IMAP4_SSL(host)
        mail.login(username,password)
        mail.select('INBOX')

        _,search_data=mail.search(None,'(FROM "order-update@amazon.in")','(FROM "order-update@amazon.in")',"UNSEEN")


        for i in search_data[0].split():
            _,data=mail.fetch(i,'(RFC822)')
            email_body=data[0][1]
            email_body=email.message_from_bytes(email_body)

if __name__=='__main__':
    read_mails()
    read_mails_1()
    read_mails_2()
    read_mails_3()
    read_mails_4()
