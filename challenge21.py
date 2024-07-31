#Eliminar registros: Escribe una consulta SQL para eliminar un usuario específico de la tabla Usuarios.
import sqlite3

#conectar a la base de datos
conn = sqlite3.connect('base_de_datos.db')
cursor = conn.cursor()


#utilizar consulta sql para eliminar un dato en la base de datos segun su id
cursor.execute('DELETE FROM Usuarios WHERE id = 1')

#guardar los datos
conn.commit()

#cerrar la conexion
conn.close()
    