from persona import Persona   # Importa la clase Persona desde el archivo persona.py

personas = []   # Lista donde se guardarán los objetos Persona creados

# Bucle principal del menú (se repetirá hasta que el usuario elija "Salir")
while True:
    print("\n==== MENU PERSONAS (SET/GET) ====")
    print("1. Crear persona")
    print("2. Mostrar lista de personas")
    print("3. Consultar persona")
    print("4. Modificar persona")
    print("5. Eliminar persona")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    
    # OPCIÓN 1: Crear una nueva persona
  
    if opcion == "1":
        print("\n--- Crear persona ---")

        p = Persona()  # Se crea un nuevo objeto Persona

        # Se asignan los valores usando los métodos setters
        p.setIdentificacion(input("Identificación: "))
        p.setNombre(input("Nombre: "))
        p.setApellido(input("Apellido: "))
        p.setEdad(int(input("Edad: ")))
        p.setCorreo(input("Correo: "))

        personas.append(p)  # Se guarda la persona en la lista
        print("Persona guardada.")

   
    # OPCIÓN 2: Mostrar todas las personas registradas

    elif opcion == "2":
        print("\n--- Lista de personas registradas ---")

        if len(personas) == 0:
            print("No hay personas registradas.")
        else:
            # Se muestra cada persona con índice
            for i, p in enumerate(personas, start=1):
                print(f"{i}. {p}")  # __str__() debe estar definido en Persona

   
    # OPCIÓN 3: Consultar una persona por su identificación
 
    elif opcion == "3":
        print("\n--- Consultar persona ---")
        ident = input("Ingrese la identificación: ")

        persona_encontrada = None

        # Buscar persona por identificación
        for p in personas:
            if p.getIdentificacion() == ident:
                persona_encontrada = p
                break

        # Mostrar resultado
        if persona_encontrada:
            print("\nPersona encontrada:")
            print(persona_encontrada)
        else:
            print("No existe ninguna persona con esa identificación.")

   
    # OPCIÓN 4: Modificar datos de una persona
    
    elif opcion == "4":
        print("\n--- Modificar persona ---")
        ident = input("Ingrese la identificación de la persona a modificar: ")

        persona_encontrada = None

        # Buscar persona
        for p in personas:
            if p.getIdentificacion() == ident:
                persona_encontrada = p
                break

        if persona_encontrada:
            print("\nDeje vacío el campo que NO desee cambiar:")

            # Para cada campo, solo se cambia si el usuario escribe algo
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

   
    # OPCIÓN 5: Eliminar persona por identificación
   
    elif opcion == "5":
        print("\n--- Eliminar persona ---")
        ident = input("Ingrese la identificación de la persona a eliminar: ")

        persona_encontrada = None

        # Buscar persona
        for p in personas:
            if p.getIdentificacion() == ident:
                persona_encontrada = p
                break

        if persona_encontrada:
            personas.remove(persona_encontrada)
            print("Persona eliminada correctamente.")
        else:
            print("No existe ninguna persona con esa identificación.")


    # Si el usuario elige una opción inválida
   
    elif opcion == "6":
        print("Saliendo del programa...")
        break  # Termina el bucle

    else:
        print("Opción no válida. Intente nuevamente.")
