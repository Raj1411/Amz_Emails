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
            st.write(i)
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
