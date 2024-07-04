from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #db se convierte en un objeto que nos permite interactuar con la base de datos

class Usuarios(db.Model): #modelo de datos gestionado por sqlalchemy
    
    #los atributos de clase definen "que datos" se van a guardar o sea columnas
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable = False)
    #atributos de instancia contienen los datos especifivos que esos campos almacenan
    def __init__(self, nombre): 
        self.nombre = nombre
        
