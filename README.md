# Email Service

Servicio para enviar plantillas de correos electronicos masivos a traves de plantillas de datos exportadas por shopify.

## Templates

Se agregan las plantillas html en la ruta src/template/
las plantillas deben ser archivos .html con las propiedades del correo electronico

## Dependencias

Antes de ejecutar el programa correr el comando para instalar sus dependencias

```bash
pip install -r requirements.txt
```

## Uso

Para utilizar el programa existen diferentes argumentos disponible para su manipulacion una vez creadas las plantillas.

con correr el comando run.py y los parametros -p para la contrasena del correo utilizado y -m para el correo electronico que se utilizara
se ejecutara el programa teniendo por defecto servidor smtp gmail, el template agregado en el repositorio y utilizara el archivo exportado por default en xlsx de shopify

### --help

El comando help dara la informacion con los argumentos disponibles para correr el comando
```bash

python run.py --help

usage: run.py [-h] [-SMTP SMTP] [-SP SMTPPORT] [-f FILE] [-m EMAIL] [-p PASSWORD] [-t TEMPLATE]

Send massive emails for shopify datasheets exports

optional arguments:
  -h, --help            show this help message and exit
  -SMTP SMTP, --smtp SMTP
                        Give SMTP server for mail sends
  -SP SMTPPORT, --smtpport SMTPPORT
                        Add port for smtp server
  -f FILE, --file FILE  Specify file root for getting mail
  -m EMAIL, --email EMAIL
                        Add email from sending
  -p PASSWORD, --password PASSWORD
                        Add password from sending email
  -t TEMPLATE, --template TEMPLATE
                        Select template to send
```
