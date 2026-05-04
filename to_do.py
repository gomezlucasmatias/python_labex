# todo_list.py
tareas = []

while True:
    print("\n--- MIS TAREAS ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        if not tareas:
            print("📭 No hay tareas pendientes")
        else:
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
    
    elif opcion == "2":
        nueva_tarea = input("Describe la tarea: ")
        tareas.append(nueva_tarea)
        print("✅ Tarea agregada")
    
    elif opcion == "3":
        if tareas:
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
            num = int(input("Número de tarea completada: ")) - 1
            if 0 <= num < len(tareas):
                completada = tareas.pop(num)
                print(f"🎉 Tarea '{completada}' completada")
            else:
                print("❌ Número inválido")
        else:
            print("No hay tareas para completar")
    
    elif opcion == "4":
        print("👋 ¡Hasta luego!")
        break
    
    else:
        print("❌ Opción no válida")
