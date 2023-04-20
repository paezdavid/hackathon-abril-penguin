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
#      cant_camas INTEGER,
#      foto TEXT
#      ) ''')


# cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas,foto) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', ('Penitenciaria Nacional de TACUMBÚ', 4000, 'AVDA SANTA TERESA', 2000, 600, 800, 3000, 'Asuncion', 'Paraguay', 2000,'https://upload.wikimedia.org/wikipedia/commons/f/f1/Tacumbu.prison.jpg') )
# cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas,foto) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', ('Penitenciaria Nacional del buen pastor ', 373, 'AVDA Mariscal Lopez', 5 , 100, 150, 400, 'Asuncion', 'Paraguay', 250,'https://cloudfront-us-east-1.images.arcpublishing.com/lanacionpy/XWA723BEBFGMJEADBGYDH5LGKA.jpg') )
# cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas,foto) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', ('Penitenciaria Juan de la Vega', 313, '12 de Octubre', 4 , 100, 80, 250, 'Emboscada', 'Paraguay', 250 ,'https://www.pj.gov.py/images/noticias/11-05-20-5eb972ba355ee-4.jpg') )
# cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas,foto) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', ('Penitenciaria Nacional de Emboscada', 726 , '12 de Octubre', 9, 300, 300, 800, 'Emboscada', 'Paraguay', 500,'https://www.itaipu.gov.br/sites/default/files/u56/emboscada_4.JPG') )
# cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas,foto) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', ('Penitenciaria Regional de Concepcion', 1000, 'Gral Bernardino Caballero', 5, 500, 400, 1200, 'Concepcion', 'Paraguay', 500,'https://www.ministeriodejusticia.gov.py/application/files/3615/2509/9073/sede_concepcion.jpeg') )
# cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas,foto) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', ('Penitenciaria Regional de Misiones', 1000, 'Ruta 1 ', 5, 500, 400, 1200, 'Misiones', 'Paraguay', 500,'https://media.ultimahora.com/p/3f164adcaf844154340bfe4178c664f3/adjuntos/161/imagenes/009/749/0009749008/penitenciaria-regional-misionesjpg.jpg') )
# cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas,foto) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', ('Penitenciaria Regional de Coronel Oviedo', 1000, 'Ruta 8 ', 5, 500, 400, 1200, 'Coronel Oviedo', 'Paraguay', 500,'https://www.lanacion.com.py/resizer/iGaPH3fVQApHrSzQu0Zp7ON9Fug=/1016x0/smart/filters:format(jpg):quality(70)/cloudfront-us-east-1.images.arcpublishing.com/lanacionpy/QSIZPHVQ5VBSHO3KQ5Y3SK2QDA') )
# cursor.execute(''' INSERT INTO penitenciarias (nombre ,cant_reclusos, direccion, cant_pabellones, cant_funcionarios, cant_celdas, capacidad, ciudad, pais,cant_camas,foto) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', ('Centro educativo itagua', 1000, 'Ruta 2 ', 5, 500, 400, 1200, 'Itagua', 'Paraguay', 500,'https://hoypyspace.sfo2.cdn.digitaloceanspaces.com/imagenes/2021/02/08130206/2011-04-07_centro-educativo-de-itaugua.jpg') )


conn.commit()
conn.close()
