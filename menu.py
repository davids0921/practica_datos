from persona import Persona

personas = []

while True:
    print("\n==== MENU PERSONAS (SET/GET) ====")
    print("1. Crear persona")
    print("2. Mostrar lista de personas")
    print("3. Consultar persona")
    print("4. Modificar persona")
    print("5. Eliminar persona")
    print("6. Salir")

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

    elif opcion == "2":
        print("\n--- Lista de personas registradas ---")

        if len(personas) == 0:
            print("No hay personas registradas.")
        else:
            for i, p in enumerate(personas, start=1):
                print(f"{i}. {p}")


    elif opcion == "3":
        print("\n--- Consultar persona ---")
        ident = input("Ingrese la identificación: ")

        persona_encontrada = None

        for p in personas:
            if p.getIdentificacion() == ident:
                persona_encontrada = p
                break

        if persona_encontrada:
            print("\nPersona encontrada:")
            print(persona_encontrada)
        else:
            print("No existe ninguna persona con esa identificación.")

    
    elif opcion == "4":
        print("\n--- Modificar persona ---")
        ident = input("Ingrese la identificación de la persona a modificar: ")

        persona_encontrada = None

        for p in personas:
            if p.getIdentificacion() == ident:
                persona_encontrada = p
                break

        if persona_encontrada:
            print("\nDeje vacío el campo que NO desee cambiar:")

            nuevo_nombre = input("Nuevo nombre: ")
            if nuevo_nombre != "":
                persona_encontrada.setNombre(nuevo_nombre)

            nuevo_apellido = input("Nuevo apellido: ")
            if nuevo_apellido != "":
                persona_encontrada.setApellido(nuevo_apellido)

            nueva_edad = input("Nueva edad: ")
            if nueva_edad != "":
                persona_encontrada.setEdad(int(nueva_edad))

            nuevo_correo = input("Nuevo correo: ")
            if nuevo_correo != "":
                persona_encontrada.setCorreo(nuevo_correo)

            print("Persona modificada correctamente.")
        else:
            print("No existe ninguna persona con esa identificación.")

    elif opcion == "5":
        print("\n--- Eliminar persona ---")
        ident = input("Ingrese la identificación de la persona a eliminar: ")

        persona_encontrada = None

        for p in personas:
            if p.getIdentificacion() == ident:
                persona_encontrada = p
                break

        if persona_encontrada:
            personas.remove(persona_encontrada)
            print("Persona eliminada correctamente.")
        else:
            print("No existe ninguna persona con esa identificación.")