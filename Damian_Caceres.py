usuarios = {}

def validar_codigo(codigo):
    tiene_mayusculas=False
    tiene_numeros=False
    for clave in codigo:
        if clave.isupper():
            tiene_mayusculas = True
        elif clave.isdigit():
            tiene_numeros = True
    if len(codigo) >= 8 and tiene_mayusculas and tiene_numeros:
        return True
    return False

def registrar_usuario():
    while True:
        nombre = input('Ingrese un nombre (no debe tener espacios.): ').strip()
        if nombre in usuarios:
            print('Este usuario ya se encuentra registrado. ')
        else:
            sexo = input('Ingrese Genero (M/F): ').upper()
            if validar_genero(sexo):
                break
    while True:
        codigo = input('Ingrese un codigo (Debe contener 8 caracteres minimo, una Mayuscula y un digito): ')
        if validar_codigo(codigo):
            print('Codigo Valido. ')
            print('Usuario registrado correctamente.')
            usuarios[nombre]={"Genero":sexo, "Codigo":codigo}
            break
        else:
            print('El codigo debe contener 8 caracteres, una mayuscula y un numero como minimo. ')

def validar_genero(sexo):
    if sexo not in ["M", "F"]:
        print('El genero debe ser M o F.')
        return False
    return True

def buscar_usuario():
    nombre = input('Ingrese el nombre a buscar: ').strip()
    if nombre in usuarios:
        print(f'El Genero es: {usuarios[nombre]['Genero']} y el Codigo es: {usuarios[nombre]['Codigo']}.')
    else:
        print('Usuario no encontrado.')

def eliminar_usuario():
    nombre = input('Ingrese el nombre a eliminar: ').strip()
    if nombre in usuarios:
        del usuarios[nombre]
        print('Usuario eliminado exitosamente.')
    else:
        print('Usuario no encontrado, no se pudo eliminar.')

def main():
    while True:
        print('*'*6+'MENU USUARIOS'+'*'*6)
        print('1. Ingresar Usuario')
        print('2. Buscar Usuario')
        print('3. Eliminar Usuario')
        print('4. Salir')
        print('*'*6+'MENU USUARIOS'+'*'*6)

        opcion = input('Ingrese una opcion (1/4): ')

        match opcion:

            case "1":
                registrar_usuario()
            case "2":
                buscar_usuario()
            case "3":
                eliminar_usuario()
            case "4":
                print('Saliendo del programa.')
                break
            case default:
                print('Opcion no valida.')

main()