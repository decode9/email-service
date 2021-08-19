## Email Service

Servicio para enviar plantillas de correos electronicos masivos a traves de plantillas de datos exportadas por shopify.

Se agregan las plantillas html en la ruta src/template/

Se corre el programa en el archivo __init__ de src modificando el siguiente elemento para obtener la plantilla

```python
def init():
    email_content = get_template('promo_template')
```

Al modificar el string 'promo_template' se tomara el template creado en la ruta descrita anteriormente.

Antes de ejecutar el programa correr el comando 
```bash
pip install -r requirements.txt
```
Para correr el archivo simplemente ejecutar el comando en la raiz del proyecto

```bash
python run.py
```