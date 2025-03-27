#Dado un código de conducta para un servidor de Discord:
#Solicite una palabra clave al usuario e imprima todas las reglas que la contengan

rules = """Respeta a los demás. No se permiten insultos ni lenguaje
ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""
key_word = input("ingrese una palabra clave: ")
for rule in rules.split("."): #separo rules por los .
    if key_word in rule.lower(): #verifico si la palabra esta, por las dudas en minuscula
        print(rule)