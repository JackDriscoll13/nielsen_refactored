import smtplib
import ssl
import time



def send_email(emails, email_to): 
    print('\tConnecting to outlook email server, Logging in with credentials ->', end = ' ' )

    context=ssl.create_default_context()
    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as s:

        s.starttls(context=context)
        s.login('sn_audience_insights@outlook.com', 'AudienceInsights1')
        print('Done. Logged in.')

        for msg in emails:
            msg_subject = msg['subject']
            print(f'\tSending email: {msg_subject} ->', end = ' ')
            s.send_message(msg, 'sn_audience_insights@outlook.com', email_to)
            time.sleep(12)
            print('Done. Sent mail.')