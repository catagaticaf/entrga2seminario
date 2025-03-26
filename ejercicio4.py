#Valide un nombre de usuario con los siguientes criterios:
#Al menos 5 caracteres.
#Contiene al menos un número.
#Contiene al menos una letra mayúscula.
#Solo puede contener letras y números.

def validarUser(user): #defino una funcion para resolver el enunciado como vimos en clase
    if len(user) < 5:   #controlo de a una las condiciones ya que cada una devuelve una rta distinta
        return "el nombre de usuario debe tener al menos 5 caracteres"
    if not any (char.isdigit() for char in user):
        return "el nombre de usuario debe contener al menos un número"
    if not any (char.isupper() for char in user):
        return "el nombre debe contener al menos una letra mayúscula"
    if not user.isalnum():
        return "la contraseña solo puede contener letras y números"
    return "nombre de usuario válido" #en caso de que no se cumpa ninguna, retorno valido

userName = input("ingrese un nombre de usuario: ")
print(validarUser(userName))