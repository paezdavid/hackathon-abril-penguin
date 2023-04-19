from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from typing import Union
from fastapi import FastAPI

app = FastAPI()

# Crear el motor
engine = create_engine('sqlite:///penitenciarias.db', echo=True)

# Crear la session factory
Session = sessionmaker(bind=engine)

# Definir la clase Base
Base = declarative_base()

# Definimos nuestro modelo de DB
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
    foto= Column(String)

# Iniciamos una sesion
session = Session()

# Traemos todos los registros
penitenciarias = session.query(Penitenciarias).all()

session.close()



@app.get("/penitenciarias")
def ver_penitenciarias():
    return {'penitenciarias': penitenciarias}


@app.get("/penitenciarias/{item_id}")
def read_item(item_id: int):
    
    for penitenciaria in penitenciarias:
        if penitenciaria.id == item_id:
            return  {
                "id": penitenciaria.id,
                "direccion": penitenciaria.direccion,
                "cant_funcionarios": penitenciaria.cant_funcionarios,
                "capacidad": penitenciaria.capacidad,
                "pais": penitenciaria.pais,
                "cant_pabellones": penitenciaria.cant_pabellones,
                "nombre": penitenciaria.nombre,
                "cant_reclusos": penitenciaria.cant_reclusos,
                "cant_celdas": penitenciaria.cant_celdas,
                "ciudad": penitenciaria.ciudad,
                "cant_camas": penitenciaria.cant_camas,
                "foto": penitenciaria.foto
            }
