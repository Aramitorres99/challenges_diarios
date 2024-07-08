# Actualizar registros: Escribe una consulta SQL para actualizar 
# el nombre de un usuario específico en la tabla Usuarios.

import sqlite3

#conectar a la base de datos
conn = sqlite3.connect('base_de_datos.db')
cursor = conn.cursor()

#hacer la actualizacion del usuario en la base de datos
cursor.execute("UPDATE Usuarios SET name = 'arami torres' where id = 1;")

#guardar los datos
conn.commit()

#cerrar la conexion
conn.close()