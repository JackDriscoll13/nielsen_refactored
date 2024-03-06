from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
from datetime import datetime

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
        note = email_notes[i]

        msg = EmailMessage()
        msg['Subject'] = str(subject) + ' - ' + str(dow) +' ' + str(dateofdata)
        msg['From'] = 'sn_audience_insights@outlook.com'
        msg['To'] = email_forward

        msg.set_content('This is a plain text body. This is placeholder text.')
        body_html = ''
        for dma in email_dmas: 
            body_html += dma_html_dict[dma]
        recipiants_sting = ','.join(recipiants)
        recipiants_string = f'<p>Email to:</p><p>{recipiants_sting}</p>'
        final_email_html = recipiants_string + note + '<hr color="black" size="2" width="100%">' + body_html

        msg.add_alternative(final_email_html, subtype='html')
        
        # Add tables
        for path in table_path_dict: 
            with open(path, 'rb') as  img:
                    maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

                    msg.get_payload()[1].add_related(img.read(), 
                                             maintype=maintype, 
                                             subtype=subtype, 
                                             cid=table_path_dict[path])
        # # Add charts
        for path in chart_path_dict: 
            with open(path, 'rb') as  img:
                    maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

                    msg.get_payload()[1].add_related(img.read(), 
                                            maintype=maintype, 
                                            subtype=subtype, 
                                            cid=chart_path_dict[path])
        
        emails.append(msg)

    return emails