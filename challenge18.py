#inserción de datos: Escribe una consulta SQL para insertar un solo registro en la tabla Usuarios.

import sqlite3

#conectar a la base de datos
conn = sqlite3.connect('base_de_datos.db')
cursor = conn.cursor()

#crear un nuevo registro 
name = 'Abril Torres'
#utilizar consulta sql para insertar un dato en la base de datos que seria "nombre"
cursor.execute('INSERT INTO Usuarios (name) VALUES (?)', (name,))

#guardar los datos
conn.commit()

#cerrar la conexion
conn.close()
    