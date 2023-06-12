import random
import string
import sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

from flask import Flask, render_template, request, redirect

# Define la base de datos
Base = sqlalchemy.orm.declarative_base()

# Define la clase que representa la tabla
class Url(Base):
    __tablename__ = 'urls'
    id_link = Column(Integer, primary_key=True)
    url_original = Column(String(255), nullable=False)
    url_recortada = Column(String(255), nullable=False)

# Crea una instancia del motor de la base de datos
engine = create_engine('mysql+mysqlconnector://root@localhost:3306/db_url')

# Crea todas las tablas definidas en la base de datos
Base.metadata.create_all(engine)

# Crea una sesión de SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

def generar_url(length=6):
    caracteres = string.ascii_letters + string.digits
    url_recortada = ''.join(random.choice(caracteres) for contador in range(length))
    return url_recortada

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