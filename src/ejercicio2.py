#encuentre el titulo con mas palabras e imprimalo en pantalla
titles = [
"Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Música en vivo: improvisaciones al piano"
]

cant = 0
max = 0
tituloMax = ""
for title in titles: #recorro la lista
    palabras = title.split() #separo en palabras
    for p in palabras: #cuento las palabras
        cant += 1
    if cant > max:     #si es el mayor reemplazo
        max = cant
        tituloMax = title #si es el mas largo reemplazo
    cant = 0 #reinicio cant
print(tituloMax)