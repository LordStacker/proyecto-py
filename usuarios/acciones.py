import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\n Ok Vamos a registrarte en el sistema...")
        nombre = input("Cual es tu nombre?: ")
        apellidos = input("Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\n No te has registrado correctamente")    
    def login(self):
        print("\n Vale, Identificate en el sistema")
        try:
            email = input("Introduce tu email: ")
            password = input("introduce tu contraseña: ")
            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()
            if email == login [3]:
                print(f"\n Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login Incorrecto!, Intentar mas tarde")
    def proximasAcciones(self,usuario):
        print("""
        Acciones disponibles:
        -Crear nota(crear)
        -Mostrar tus notas (mostrar)
        -Eliminar nota (eliminar)
        -Salir (salir)
        """)
        accion = input("Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        
        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"\n Ok {usuario[1]}, hasta pronto!!")
            exit()