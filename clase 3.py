# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingresa tu edad: ")
rol = input("Ingresa tu rol (estudiante/docente/otro): ").lower()

# Validar edad como número entero
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Error: la edad debe ser un numero entero. ")

# Evaluar condiciones
if edad >= 18 and (rol == "estudiante" or rol == "docente"):
     print(f"Permitido el acceso, {nombre}.")
     print("Puedes acceder a la actividad.")

elif edad <18:
    print("No permitido el acceso.")

es_estudiante = True
es_docente = True
es_otro = False

if es_estudiante or es_docente:
    print("Permitido el acceso")
else:
    print("No permitido el acceso")