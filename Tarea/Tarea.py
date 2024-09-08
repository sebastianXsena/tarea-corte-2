
class Usuario:
    def __init__(self, NombreCompleto, NickName, Clave, Tipo, Fecha_Creacion):
        
        self.datos = {
            "Nombre Completo": NombreCompleto,
            "NickName": NickName,
            "Clave": Clave,
            "Tipo": Tipo,
            "Fecha de Creación": Fecha_Creacion
        }


def agregar_usuario(usuarios):
    NombreCompleto = input("Ingrese su nombre completo: ")
    Nickname = input("Ingrese el Nickname: ")
    Clave = input("Ingrese la Clave: ")
    Tipo = input("Ingrese el tipo de usuario: ")
    Fecha_Creacion = input("Ingrese su fecha de creación de cuenta (Mes/Día/Año): ")

    nuevo_usuario = Usuario(NombreCompleto, Nickname, Clave, Tipo, Fecha_Creacion)
    usuarios.append(nuevo_usuario)
    print("El usuario fue agregado\n")


def eliminar_usuario(usuarios, valor):
    for i, usuario in enumerate(usuarios):
        if valor in usuario.datos.values():
            del usuarios[i]
            print("El usuario fue eliminado.")
            return True
    return False


def buscar_usuario(usuarios, valor):
    for usuario in usuarios:
        if valor in usuario.datos.values():
            return usuario.datos
    return None


def menu():
    usuarios = []

    while True:
        print("Menu")
        print("1.) Agregar Usuario")
        print("2.) Buscar Usuario")
        print("3.) Eliminar Usuario")
        print("4.) Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_usuario(usuarios)
        elif opcion == '2':
            valor_buscar = input("Ingrese el valor a buscar: ")
            resultado = buscar_usuario(usuarios, valor_buscar)
            if resultado:
                print("Usuario encontrado:", resultado)
            else:
                print("Usuario no encontrado.")
        elif opcion == '3':
            valor_eliminar = input("Ingrese el valor del usuario a eliminar: ")
            if not eliminar_usuario(usuarios, valor_eliminar):
                print("Usuario no encontrado o no se pudo eliminar.")
        elif opcion == '4':
            print("Cerrando el programa")
            break
        else:
            print("Opción no válida, escoja otra opcion.")

menu()



