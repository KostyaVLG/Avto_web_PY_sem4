import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def sendemail():
    fromaddr = 'sidnirova@mail.ru'
    toaddr = 'sidnirova@mail.ru'
    mypass = 'BrHwnhJhjqGakXufPSHP'
    reportname = 'log.txt'

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Привет от меня'
    with open(reportname, 'rb') as f:
        part = MIMEApplication(f.read(), Name=basename(reportname))
        part['Content_Disposition'] = 'attachment; filename="%s"' % basename(reportname)
        msg.attach(part)

    body = 'Это тестовое сообщение'
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

if __name__ == '__main__':
    sendemail()