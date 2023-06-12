from flask import Flask, render_template, request, redirect

from db import session, Url, engine, Base
from utils import generar_url

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    url_recortada = None
    url_original = None
    if request.method == 'POST':
        url_original = request.form.get('url_original')
        url_recortada = generar_url()
        while session.query(Url).filter_by(url_recortada=url_recortada).first() is not None:
            url_recortada = generar_url()

        url = Url(url_original=url_original, url_recortada=url_recortada)

        session.add(url)
        session.commit()

        url_recortada = request.url_root + url_recortada
        url_original = url_original

    return render_template('index.html', url_recortada=url_recortada, url_original=url_original)

@app.route('/<url_recortada>')
def redireccionar_url(url_recortada): 
    url = session.query(Url).filter_by(url_recortada=url_recortada).first()

    if url:
        return redirect(url.url_original)
    else:
        return "URL no encontrada", 404
    
@app.route('/urls')
def mostrar_urls():
    urls = session.query(Url).all()
    return render_template('urls.html', urls=urls)


if __name__ == '__main__':
    app.run(debug=True)
