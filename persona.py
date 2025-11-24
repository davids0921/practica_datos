class Persona:
    def __init__(self):
        # Constructor: inicializa los atributos de la persona
        self.identificacion = ""   # Identificación única de la persona
        self.nombre = ""           # Nombre de la persona
        self.apellido = ""         # Apellido de la persona
        self.edad = 0              # Edad de la persona
        self.correo = ""           # Correo electrónico de la persona


    #          SETTERS
    # Métodos que permiten asignar valores a los atributos

    def setIdentificacion(self, valor):
        self.identificacion = valor

    def setNombre(self, valor):
        self.nombre = valor

    def setApellido(self, valor):
        self.apellido = valor

    def setEdad(self, valor):
        self.edad = valor

    def setCorreo(self, valor):
        self.correo = valor

    
    #          GETTERS
    # Métodos para obtener el valor de cada atributo
 
    def getIdentificacion(self):
        return self.identificacion

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getEdad(self):
        return self.edad

    def getCorreo(self):
        return self.correo

    # Método para retornar los datos en forma de diccionario
  
    
    def consultarPersona(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "correo": self.correo
        }

    
    # Método especial __str__
    # Convierte el objeto en una cadena legible
    # Cuando imprimes el objeto, se muestra este formato
   
    def __str__(self):
        return (f"ID: {self.identificacion}, "
                f"Nombre: {self.nombre} {self.apellido}, "
                f"Edad: {self.edad}, "
                f"Correo: {self.correo}")
