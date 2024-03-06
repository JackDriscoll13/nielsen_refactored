from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
import smtplib


def get_email_html(email_dmas, dma_html_dict, table_path_dict): 

    msg = EmailMessage()
    msg['Subject'] = 'This is the second version of a test.'
    msg['From'] = 'sn_audience_insights@outlook.com'
    msg['To'] = 'jack.driscoll@charter.com'

    msg.set_content('This is a plain text body. This is a test.')
    email_html = ''
    for dma in email_dmas: 
        email_html += dma_html_dict[dma]

    msg.add_alternative(email_html, subtype='html')
    
    # Add tables
    for path in table_path_dict: 
        with open(path, 'rb') as  img:
                print(f'attaching image: \n{path}')
                maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

                msg.get_payload()[1].add_related(img.read(), 
                                         maintype=maintype, 
                                         subtype=subtype, 
                                         cid=table_path_dict[path])
    # # Add charts
    # for path in chart_path_dict: 
    #     with open(path, 'rb') as  img:
    #             print(f'attaching image: \n{path}')
    #             maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

    #             msg.get_payload()[1].add_related(img.read(), 
    #                                      maintype=maintype, 
    #                                      subtype=subtype, 
    #                                      cid=chart_path_dict[path])


    print('Connecting to email server')
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login('sn_audience_insights@outlook.com', 'AudienceInsights1')
    print('\nlogged in..., sending mail...\n ')
    s.send_message(msg, 'sn_audience_insights@outlook.com', 'jack.driscoll@charter.com',)
    print('Sent mail')
    s.quit()
    