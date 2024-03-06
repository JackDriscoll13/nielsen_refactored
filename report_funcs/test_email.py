
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
import smtplib


def test_smtp():

    
        # Attempt 2 
        msg = EmailMessage()
        msg['Subject'] = 'Hello there, this is a test'
        msg['From'] = 'sn_audience_insights@outlook.com'
        msg['To'] = 'jack.driscoll@charter.com'

        msg.set_content('This is a plain text body. This is a test.')
        


        image_cid = make_msgid()
        image_cid2 = make_msgid()

        print(image_cid)
        print(image_cid2)

        # if `domain` argument isn't provided, it will 
        # use your computer's name
        print("creating body..")
        newbody = """
                <html>
                    <body>
                        <p>This is an HTML body.<br>
                        It also has an image.
                        </p>
                        <img src="cid:{image_cid}">
                        <p>This is an HTML body.<br>
                        It also has an image.
                        </p>
                        <img src="cid:{image_cid2}">
                    </body>
                </html>
            """.format(image_cid=image_cid[1:-1], image_cid2 = image_cid2[1:-1])
        

        msg.add_alternative(newbody, subtype='html')
        print(image_cid)

        with open('C:/Users/P3159331/OneDrive - Charter Communications/Documents - Audience Insights/5. Development/Nielsen Automation/nielsen_refactored/chart_images2/S1TPtable.png', 'rb') as  img:
                print('attaching emails')
        # know the Content-Type of the image
                maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

                msg.get_payload()[1].add_related(img.read(), 
                                         maintype=maintype, 
                                         subtype=subtype, 
                                         cid=image_cid)


        with open('C:/Users/P3159331/OneDrive - Charter Communications/Documents - Audience Insights/5. Development/Nielsen Automation/nielsen_refactored/chart_images2/S1TPchart.png', 'rb') as  img:
                print('attaching emails2 ')
                maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

                msg.get_payload()[1].add_related(img.read(), 
                                         maintype=maintype, 
                                         subtype=subtype, 
                                         cid=image_cid2)

        import smtplib
        print('Connecting to email server')
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
        s.login('sn_audience_insights@outlook.com', 'AudienceInsights1')
        print('\nlogged in..., sending mail...\n ')
        s.send_message(msg, 'sn_audience_insights@outlook.com', 'jack.driscoll@charter.com',)
        print('Sent mail')
        s.quit()
        
if __name__ == '__main__':
       test_smtp()
