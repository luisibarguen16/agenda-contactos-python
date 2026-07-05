
# Agenda de contactos
#permite agregar, mostrar y borrar datos usando un diccionario

print("------Agenda de contactos-------\n")

agenda = {}

def agregar_datos():

    nombre = input("Escribe tu nombre: ").capitalize().strip()
    telefono = input("Escribe tu número de teléfono: ").replace(" ", "")

    if nombre == "" or telefono == "":
        print("No has escrito ningún nombre o teléfono, vuelve a intentarlo")
        return
    
    if not telefono.isdigit():
        print("El teléfono solo puede tener números") 
        return
    
    if len(telefono) != 11:
        print("El número de teléfono debe tener 11 dígitos")
        return
    
    agenda[nombre] = telefono
    print("Elemento agregado correctamente.")

def mostrar_datos():

    if not agenda:
        print("La agenda está vacía")
        return
    
    
    print("----Datos guardados----\n")
    for clave, valor in agenda.items():
        print(f"{clave}: {valor}")

def eliminar_datos():

    nombre = input("Escribe el nombre que quieres eliminar de la agenda: ").capitalize().strip()

    if nombre == "":
        print("Debes escribir un nombre")
        return
    
    if nombre not in agenda:
        print("Nombre no encontrado en la agenda")
        return
    
    agenda.pop(nombre)
    print("Elemento eliminado correctamente.")



while True:
    print("---Menú---\n")

    print("Escribe (agregar), si quieres introducir datos nuevos a la agenda")
    print("Escribe (mostrar), si quieres ver los datos guardados en la agenda")
    print("Escribe (borrar), si quieres eliminar elementos de la agenda")
    print("Escribe (salir), si no quieres estar más en la agenda\n")

    opcion = input("Escribe lo que quieres realizar: ").strip().lower()

    if opcion == "agregar":
        agregar_datos()

    elif opcion == "mostrar":
        mostrar_datos()

    elif opcion == "borrar":
        eliminar_datos()

    elif opcion == "salir":
        print("Gracias por usar el programa.")
        break
    else:
        print("Respuesta inválida, vuelve a intentarlo.")
