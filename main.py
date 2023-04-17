from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Create the engine
engine = create_engine('sqlite:///penitenciarias.db', echo=True)

# Create a session factory
Session = sessionmaker(bind=engine)

# Define the Base class
Base = declarative_base()

class Penitenciarias(Base):
    __tablename__ = "penitenciarias"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    cant_reclusos = Column(Integer)
    direccion = Column(String)
    cant_pabellones = Column(Integer)
    cant_funcionarios = Column(Integer)
    cant_celdas = Column(Integer)
    capacidad = Column(Integer)
    ciudad = Column(String)
    pais = Column(String)
    cant_camas = Column(Integer)


session = Session()


penitenciarias = session.query(Penitenciarias).all()
session.close()
for penitenciaria in penitenciarias:
    print(penitenciaria.nombre)


# print(penitenciarias)
