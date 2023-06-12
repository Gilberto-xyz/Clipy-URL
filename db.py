import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

# Crea una instancia del motor de la base de datos
engine = create_engine('mysql+mysqlconnector://root@localhost:3306/db_url', echo=True)

# Crea una sesión de SQLAlchemy para permitir la comunicación con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Define la base de datos
Base = sqlalchemy.orm.declarative_base()

# Define la clase que representa la tabla
class Url(Base):
    __tablename__ = 'urls'
    id_link = Column(Integer, primary_key=True)
    url_original = Column(String(255), nullable=False)
    url_recortada = Column(String(255), nullable=False)

# Crea todas las tablas definidas en la base de datos
Base.metadata.create_all(engine)

