#Creación de tabla: Escribe una consulta SQL para crear una tabla Usuarioscon columnas id y nombre.
import sqlite3

# Conectar a la base de datos 
conn = sqlite3.connect('base_de_datos.db')
cursor = conn.cursor()

# Crear la tabla Usuarios
cursor.execute('''
CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')
#guardar los datos
conn.commit()
#cerrar la conexion
conn.close()
    
        
