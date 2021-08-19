from email.message import Message

def construct_message(subject, to, fro, email_content):
    msg = Message()
    msg['Subject'] = subject
    msg['From'] = fro
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)
    msg['To'] = to
    return msg
