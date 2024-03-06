import smtplib

def send_email(msg, email_to): 
    print('Connecting to email server')
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login('sn_audience_insights@outlook.com', 'AudienceInsights1')
    print('\nlogged in..., sending mail...\n ')
    s.send_message(msg, 'sn_audience_insights@outlook.com', email_to)
    print('Sent mail')
    s.quit()