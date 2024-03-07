import smtplib
import time

def send_email(emails, email_to): 
    print('\tConnecting to outlook email server, Logging in with credentials ->', end = ' ' )
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.connect("smtp-mail.outlook.com",587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('sn_audience_insights@outlook.com', 'AudienceInsights1')
    print('Done. Logged in.')

    for msg in emails:
        msg_subject = msg['subject']
        print(f'\tSending email: {msg_subject} ->', end = ' ')
        s.send_message(msg, 'sn_audience_insights@outlook.com', email_to)
        time.sleep(12)
        print('Done. Sent mail.')
    s.quit()