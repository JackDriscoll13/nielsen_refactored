from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
import smtplib
import datetime

def get_email_html(dmalists, email_forward, daily_data_15min,
                   email_recipiants, email_subjects, email_notes,
                   dma_html_dict, chart_path_dict, table_path_dict): 

    emails = []
    # Calculate 
    dateofdata = str(daily_data_15min['Dates'].unique()[0])
    dow = datetime.strptime(dateofdata,'%m/%d/%Y').strftime('%A')

    for i in range(len(dmalists)):
        email_dmas = dmalists[i]
        subject = email_subjects[i]
        recipiants = email_recipiants[i]

        msg = EmailMessage()
        msg['Subject'] = str(subject) + ' - ' + str(dow) +' ' + str(dateofdata)
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
        for path in chart_path_dict: 
            with open(path, 'rb') as  img:
                    print(f'attaching image: \n{path}')
                    maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

                    msg.get_payload()[1].add_related(img.read(), 
                                            maintype=maintype, 
                                            subtype=subtype, 
                                            cid=chart_path_dict[path])