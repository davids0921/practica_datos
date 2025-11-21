from persona import Persona

personas = []

while True:
    print("\n==== MENU PERSONAS (SET/GET) ====")
    print("1. Crear persona")
    print("2. Mostrar lista de personas")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\n--- Crear persona ---")

        p = Persona()

        p.setIdentificacion(input("Identificación: "))
        p.setNombre(input("Nombre: "))
        p.setApellido(input("Apellido: "))
        p.setEdad(int(input("Edad: ")))
        p.setCorreo(input("Correo: "))

        personas.append(p)
        print("Persona guardada.")

    