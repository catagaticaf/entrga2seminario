#Determine si dos palabras ingresadas son anagramas (contienen las mismas letras en
#diferente orden).

def anagramas(p1, p2): #hago slicing como vimos en la clase de teoría:
    p1invert = p1[::-1] #invierto la palabra
    if p1invert == p2:
        return f'{p1} y {p2} son anagramas.'
    return "No son anagramas."

p1 = input("ingrese una palabra: ")
if (p1 != "" and not p1.isdigit()): #checkeo que ingresen algo valido:
    p2 = input("ingrese la segunda palabra: ")
    if (p2 != "" and not p2.isdigit()):
        print(anagramas(p1,p2)) 
    else:
        print("no ingresó una palabra valida")
else:
    print("no ingresó una palabra valida")


