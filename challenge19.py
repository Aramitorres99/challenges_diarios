#Consulta básica: Escribe una consulta SQL para seleccionar todos los registros de la tabla Usuarios.

import sqlite3

#conectar a la base de datos
conn = sqlite3.connect('base_de_datos.db')
cursor = conn.cursor()

#hacer la consulta
cursor.execute("SELECT * FROM Usuarios")

#obtener los registros seleccionados
rows = cursor.fetchall()

#imprimir los registros seleccionados
for row in rows:
    print(row)

#cerrar la conexion
conn.close()
    