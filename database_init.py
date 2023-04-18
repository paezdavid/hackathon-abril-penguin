import sqlite3

conn=sqlite3.connect("penitenciarias.db")

cursor=conn.cursor()
cursor.execute('''
    CREATE TABLE penitenciarias
    (id INTEGER PRIMARY KEY,
    nombre TEXT,
     cant_reclusos INTEGER,
     direccion TEXT, 
     cant_pabellones INTEGER,
     cant_funcionarios INTEGER,
     cant_celdas INTEGER,
     capacidad INTEGER, 
     ciudad TEXT,
     pais TEXT,
<<<<<<< HEAD
     cant_camas INTEGER,
     foto TEXT
=======
>>>>>>> 712a0ca70b1945b8b2629abb4c4f314ac3537905
     ) ''')

# with open('tacumbu.jpg','rb') as f:
#     foto_tacumbu= f.read()

cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas,foto) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', ('Penitenciaria TACUMBÚ', 4000, 'AVDA SANTA TERESA', 2000, 600, 800, 3000, 'Asuncion', 'Paraguay', 7,'https://media.ultimahora.com/p/651b5a248dd33f0a09d4ac6c6a4fa764/adjuntos/161/imagenes/009/817/0009817748/carcel-el-buen-pastor-se-encuentra-una-zona-cotizada-asuncion.jpg') )

#FALTA AGG BIEN LAS FOTOS

# cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas,foto) VALUES (?,?,?,?,?,?,?,?,?,?)''', ('carcel2', 4000, 'AVDA SANTA TERESA', 2000, 600, 800, 3000, 'Asuncion', 'Paraguay', 7) )

# cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas,foto) VALUES (?,?,?,?,?,?,?,?,?,?)''', ('carcel2', 4000, 'AVDA SANTA TERESA', 2000, 600, 800, 3000, 'Asuncion', 'Paraguay', 7) )

# cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas) VALUES (?,?,?,?,?,?,?,?,?,?)''', ('carcel2', 4000, 'AVDA SANTA TERESA', 2000, 600, 800, 3000, 'Asuncion', 'Paraguay', 7) )

# cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas) VALUES (?,?,?,?,?,?,?,?,?,?)''', ('carcel2', 4000, 'AVDA SANTA TERESA', 2000, 600, 800, 3000, 'Asuncion', 'Paraguay', 7) )


# cursor.execute(''' DELETE FROM penitenciarias WHERE id= 1  ''') POR SI HAY QUE BORRAR ALGO MAS 

conn.commit()
conn.close()
