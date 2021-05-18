import notas.nota as modelo


class Acciones:
    def crear(self, usuario):
        print(f"\n ok {usuario[1]}!! Vamos a crear una nueva nota...")
        titulo = input("\n Introduce el titulo de tu nota:")
        descripcion = input("Mete el contenido de tu nota: ")
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        if guardar[0] >= 1:
            print(f"\n perfecto has guardado la nota: {nota.titulo}")
        else:
            print(f"\n No se ha guardado la nota, lo siento {usuario[1]}")
    def mostrar(self, usuario):
        print(f"\n Vale {usuario[1]}!! aqui tienes tus notas: ")
        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.listar()
        for nota in notas:
            print("\n ********************")
            print(nota[2])
            print(nota[3])
            print("\n ********************")
    def borrar(self, usuario):
        print(f"\n Okey {usuario[1]} vamos a borrar notas")
        titulo = input("Introduce el titulo de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()
        if eliminar [0] >= 1:
            print(f"Hemos eliminado la nota: {nota.titulo}")
        else:
            print("No se a borrado la nota, intente mas tarde...")
            