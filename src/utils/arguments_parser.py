#Importando modulo predeterminado de python para declaracion de argumentos del sistema
import argparse

#Declarando descripcion del script para su uso
text = 'Send massive emails for shopify datasheets exports'

#declaracion inicial de los argumentos a utilizar en el programa
parser = argparse.ArgumentParser(description=text)

#Agregar argumentos a utilizar en el programa
parser.add_argument("-SMTP", "--smtp", help="Give SMTP server for mail sends", default="smtp.gmail.com")
parser.add_argument("-SP", "--smtpport", help="Add port for smtp server", default='587')
parser.add_argument("-f", "--file", help="Specify file root for getting mail", default="customers_export_1.xlsx")
parser.add_argument("-m", "--email", help="Add email from sending", default='correo@gmail.com')
parser.add_argument("-p", "--password", help="Add password from sending email", default="root")
parser.add_argument("-t", "--template", help="Select template to send", default="promo_template")

#Inicializando los argumentos declarados y agregandolo a la variable arguments
arguments = parser.parse_args()