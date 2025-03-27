#Genere un código de descuento aleatorio para un usuario en base a su nombre, la fecha
#actual y el resto deben ser números o letras aleatorias. El código debe tener una longitud de
#30 caracteres, todas las letras deben ser mayúsculas.
#El usuario debe ingresarse por teclado y debe validar que no exeda los 15 caracteres.

import random
import string
def codeGenerator(usuario, fecha):
    usuario = usuario.upper()
    fecha = fecha.replace("-","") #reemplaza los guiones de la cadena por nada. Antes hice strip("-") pero me eliminaba solo el del principio y el final
    cant = 30 - len(usuario) - len(fecha) - 2 #2 es para los guiones
    letras_y_num = random.choices(string.ascii_uppercase + string.digits ,k=cant) #cant son la cantidad de digitos que me faltan para llegar a 30
    return f'{usuario}-{fecha}-{''.join(letras_y_num)}' #uso join porque lo que se genero arriba es una LIST y necesito unirlo

def validarUser(user):
    if len(user) <= 15:
        print("usuario valido")
        return True
    print("USUARIO INVÁLIDO. Ingrese un usuario válido que contenga menos de 15 caracteres")
    return False

user = input("ingrese su nombre de usuario: ")
if (validarUser(user)):
    fecha = input("ingrese la fecha en el formado AAAA-MM-DD: ")
    print(f'su código de descuento es: ', codeGenerator(user,fecha))
    
