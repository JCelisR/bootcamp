acceso = True

while acceso:
    acceso = input("Deseo iniciar el sistema de control académico (S/N): ")
    if acceso == "S":
        print("Iniciando sistema...")
        break
    elif acceso == "N":
        print("Saliendo del programa")
        exit()
    else:
        print("Opción no válida. Ingreso (S o N)")

