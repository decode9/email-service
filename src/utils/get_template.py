
def get_template(file):
    with open('src/template/{}.html'.format(file), 'r') as f:
        html_string = f.read()
    return html_string