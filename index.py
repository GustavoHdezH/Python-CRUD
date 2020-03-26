import sqlite3

"""
Ejemplo de un CRUD con Python
author = GustavoHdezH
"""
#Creaciòn de variable para conectar con la dB
conectar = sqlite3.connect('registro.db')

"""
Creaciòn Tabla 
"""
# Validar la creaciòn de una tabla 
#try:
#    operacion = conectar.cursor()
#    operacion.execute(''' 
#        CREATE TABLE alumnos (
#            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
#            nombre TEXT(20) NOT  NULL,
#            a_paterno TEXT(20) NOT NULL,
#            calificion INTEGER
#        );
#    ''')
#    print("Tabla creada correctamente")
#except:
#    print("Error al crear la tabla")
#finally:
#    conectar.close()

"""
Create Record 
"""
insert = "INSERT INTO alumnos (nombre,a_paterno,calificion) VALUES (?,?,?)"
persons = [('Dorian','Hernandez',3)]
try:
    operacion = conectar.cursor()
    operacion.executemany(insert,persons)
    conectar.commit()
    print("Creaciòn de registro exitoso")
except:
    print("Error en la operaciòn: No se pudo insertar dato")
    conectar.rollback()
finally:
    conectar.close()
