import email
import mimetypes
import email
import email.mime
import email.mime.text

import email.generator

def create_html_body_email(i, dmalists, alldmas, emailrecipaints, emailsubjects, emailnotes, emailattachments):
        dmaList = dmalists[i]
        emailto = emailrecipaints[i]
        emailsubject = emailsubjects[i]
        emailnote = emailnotes[i]
        attachments = emailattachments[i]


        bodyhtml = ''
        for dma in dmaList:
            bodyhtml += alldmas[dma]
        finalhtml =  '<html><body>' + emailnote + '<hr color="black" size="2" width="100%">' + bodyhtml +'</body></html'

        file = open(f"html_outputs/test{i}.html","w") 
        file.write(finalhtml)
        file.close()

        # Testing the .eml format
        msg = email.mime.text.MIMEText(finalhtml)
        msg['Subject'] = 'Test message'
        msg['From'] = 'sender@sending.domain'
        msg['To'] = 'rcpt@receiver.domain'

        # open a file and save mail to it
        with open(f'html_outputs/test{i}.elm', 'w') as out:
            gen = email.generator.Generator(out)
            gen.flatten(msg)