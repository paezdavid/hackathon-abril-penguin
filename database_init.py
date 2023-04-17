import sqlite3

conn=sqlite3.connect("penitenciarias.db")

cursor=conn.cursor()
# cursor.execute('''
#     CREATE TABLE penitenciarias
#     (id INTEGER PRIMARY KEY,
#     nombre TEXT,
#      cant_reclusos INTEGER,
#      direccion TEXT, 
#      cant_pabellones INTEGER,
#      cant_funcionarios INTEGER,
#      cant_celdas INTEGER,
#      capacidad INTEGER, 
#      ciudad TEXT,
#      pais TEXT,
#      cant_camas INTEGER
#      ) ''')


cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas) VALUES (?,?,?,?,?,?,?,?,?,?)''', ('Penitenciaria TACUMBÚ', 4000, 'AVDA SANTA TERESA', 2000, 600, 800, 3000, 'Asuncion', 'Paraguay', 7) )

cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas) VALUES (?,?,?,?,?,?,?,?,?,?)''', ('carcel2', 4000, 'AVDA SANTA TERESA', 2000, 600, 800, 3000, 'Asuncion', 'Paraguay', 7) )

cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas) VALUES (?,?,?,?,?,?,?,?,?,?)''', ('carcel2', 4000, 'AVDA SANTA TERESA', 2000, 600, 800, 3000, 'Asuncion', 'Paraguay', 7) )

cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas) VALUES (?,?,?,?,?,?,?,?,?,?)''', ('carcel2', 4000, 'AVDA SANTA TERESA', 2000, 600, 800, 3000, 'Asuncion', 'Paraguay', 7) )

cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas) VALUES (?,?,?,?,?,?,?,?,?,?)''', ('carcel2', 4000, 'AVDA SANTA TERESA', 2000, 600, 800, 3000, 'Asuncion', 'Paraguay', 7) )


# cursor.execute(''' DELETE FROM penitenciarias WHERE id= 1  ''') POR SI HAY QUE BORRAR ALGO MAS 

conn.commit()
conn.close()
