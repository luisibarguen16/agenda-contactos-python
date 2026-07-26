class Libro:
    # creamos un constructor llamado libro
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
 
        if self.disponible:
            self.disponible = False
            print("Libro prestado, exitosamente")
        
        else:
            print("El libro ya fue prestado.")


    def devolver(self):

        usuario = input("en serio quieres devolver el libro, (SI o NO): ").lower()
        if usuario == "":
            print("Debes escribir una respuesta, válida")
            return

        if usuario == "no":
            print("Gracias por tu respuesta.")

        elif usuario == "si" and not self.disponible:
            self.disponible = True
            print("El libro fue devuelto, correctamente.")

        elif usuario == "si" and self.disponible:
            print("El libro ya está disponible.")

        else:
            print("Respuesta incorrecta.")


    def mostrar_estado(self):

        if self.disponible:
            estado = "Disponible"

        else:
            estado = "Prestado"

        print(f" Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Estado: {estado}")

titulo = input("Escribe el titulo del libro: ")
autor = input("Escribe el, autor del libro: ")

biblioteca = Libro(titulo, autor)


while True:
    # creamos un menú
    print("\nSi quieres prestar un libro escribe: prestar")
    print("Si quieres devolver el libro escribe: devolver")
    print("Si quieres ver el estado del libro escribe: mostrar")
    print("Si quieres salir del programa escribe: salir\n")

    
    opcion = input("Escribe tu respuesta: ").lower()
    if opcion == "":
        print("Debes escribir una respuesta, válida")
        continue

    if opcion == "prestar":
        biblioteca.prestar()

    elif opcion == "devolver":
        biblioteca.devolver()

    elif opcion == "mostrar":
        biblioteca.mostrar_estado()

    elif opcion == "salir":
        break
    else:
        print("Respuesta incorrecta, vuelve a intentarlo.")