# APIPP (API de Penitenciarias Paraguayas)

## Descripción del Proyecto: 
APIPP centraliza datos del sistema penitenciario del Paraguay, promueve la transparencia de la información y hace estos datos de libre acceso al público general. La accesibilidad a estos datos ayudará principalmente a la agilización de sistemas nacionales, a analistas y a investigadores.

## Inicializar el proyecto
```git clone https://github.com/paezdavid/hackathon-abril-penguin.git```

```cd hackathon-abril-penguin```


#### Linux 
- Inicializar entorno virtual: 
```python -m venv venv```

- Activar el entorno virtual: 
```source venv/bin/activate```

- Instalar dependencias: 
```pip install -r requirements.txt```

- Crear el archivo de la base de datos: 
```python database_init.py```


#### Windows
- Inicializar entorno virtual: 
```python3 -m venv venv```

- Activar el entorno virtual: 
```.\venv\Scripts\activate```

- Instalar dependencias: 
```pip install -r requirements.txt```

- Crear el archivo de la base de datos: 
```python3 database_init.py```


#### Levantar servidores

- Flask: 
```flask --debug run```


- Ir a: 
```http://localhost:5000```


- FastAPI: 
```uvicorn main:app --reload```


- Ir a: 
```http://localhost:8000```
