class Persona:
    def __init__(self):
        self.identificacion = ""
        self.nombre = ""
        self.apellido = ""
        self.edad = 0
        self.correo = ""

    # SETTERS
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

    # GETTERS
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

 
    def consultarPersona(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "correo": self.correo
        }

    def __str__(self):
        return (f"ID: {self.identificacion}, "
                f"Nombre: {self.nombre} {self.apellido}, "
                f"Edad: {self.edad}, "
                f"Correo: {self.correo}")
