def lista_de_tareas():
    tareas = []

    def mostrar_menu():
        print("""
        --- Lista de Tareas ---
        1. Agregar tarea
        2. Ver tareas
        3. Eliminar tarea
        4. Modificar tarea
        5. Salir 
        """)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tarea = input("Introduce la tarea: ")
            tareas.append(tarea)
            print("Tarea agregada.")
        elif opcion == "2":
            if tareas:
                print("\nTareas:")
                for i, tarea in enumerate(tareas, start=1):
                    print(f"{i}. {tarea}")
            else:
                print("No hay tareas.")
        elif opcion == "3":
            tarea = input("Introduce la tarea a eliminar: ")
            if tarea in tareas:
                tareas.remove(tarea)
                print("Tarea eliminada.")
            else:
                print("Tarea no encontrada.")
        elif opcion == "4":
            tarea_vieja = input("Introduce la tarea a modificar: ")
            if tarea_vieja in tareas:
                tarea_nueva = input("Introduce la nueva tarea: ")
                indice = tareas.index(tarea_vieja)
                tareas[indice] = tarea_nueva
                print("Tarea modificada.")
            else:
                print("Tarea no encontrada.")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
           

lista_de_tareas()