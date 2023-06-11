import random
import string

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

urls_recortadas = {}

def generar_url(length=6):
    caracteres = string.ascii_letters + string.digits
    url_recortada = ''.join(random.choice(caracteres) for contador in range(length))
    return url_recortada

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url_original = request.form.get('url_original')
        url_recortada = generar_url()
        while url_recortada in urls_recortadas:
            url_recortada = generar_url()

        urls_recortadas[url_recortada] = url_original
        return render_template('index.html', url_recortada=request.url_root + url_recortada, url_original=url_original)
    return render_template('index.html')

@app.route('/<url_recortada>')
def redireccionar_url(url_recortada): 
    url_original = urls_recortadas.get(url_recortada)
    if url_original:
        return redirect(url_original)
    else:
        return "URL no encontrada", 404

if __name__ == '__main__':
    app.run(debug=True)