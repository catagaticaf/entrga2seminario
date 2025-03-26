#Dado el tiempo de reacción de un jugador en milisegundos, clasifíquelo en las siguientes categorías
#Menos de 200 ms: Rápido
#Entre 200 y 500 ms: Normal
#Más de 500 ms: Lento

def clasificar(time):
    if time < 200:
        return "categoría: Rápido"
    elif (time >= 200) & (time <=500):
        return "categoría: Normal"
    else:
        return "categoría: Lento"

time = int(input("ingrese su tiempo de reacción en ms: "))
print(clasificar(time))