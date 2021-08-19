
from .utils import get_template, start_mail_server, arguments, init_workbook, construct_message


def get_remitents(row):
    remitents = []
    count = 0

    for value in row:
        if value[2] != None:
            count += 1
            remitents.append(value[2])

    return [['jorgebastidas9@gmail.com'], count]


def init():
    email_content = get_template(arguments.template)

    config = {
        'host': arguments.smtp,
        'port': arguments.smtpport,
        'email': arguments.email,
        'password': arguments.password
    }

    mail_server = start_mail_server(**config)

    excel_workbook = init_workbook(arguments.file)
    excel_sheet = excel_workbook.active
    row_sheet = excel_sheet.iter_rows(min_row=1, values_only=True)
    remitentsData = get_remitents(row_sheet)
    remitents = remitentsData[0]
    count = remitentsData[1]

    for to in remitents:
        msg = construct_message(
            'Promocion - Codigo De Descuento!', to, arguments.email, email_content)
        mail_server.sendmail(msg['From'], [msg['To']],
                             msg.as_string().encode('utf-8'))
        print('successfully sent email to {}:'.format(msg['To']))
    mail_server.quit()
    print('Sended {} mails'.format(count))
