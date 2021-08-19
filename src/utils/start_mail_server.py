import smtplib

def start_mail_server(**args):
    host = args['host']
    port = args['port']
    password = args['password']
    email = args['email']
    
    s = smtplib.SMTP('{}:{}'.format(host, port))
    s.starttls()
    s.login(email, password)
    return s