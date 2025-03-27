#Dadas varias descripciones de streams en Twitch, cuente cuántas menciones hay de
#"entretenimiento", "música" y "charla".

descriptions = [
"Streaming de música en vivo con covers y composiciones",
"Charla interactiva con la audiencia sobre series y películas",
"Jugamos a juegos retro y charlamos sobre su historia",
"Exploramos la mejor música de los 80s y 90s",
"Programa de entretenimiento con noticias y curiosidades del mundo gamer",
"Sesión de charla con invitados especiales del mundo del streaming",
"Música en directo con improvisaciones y peticiones del chat",
"Un espacio para charlar relajada sobre tecnología y cultura digital",
"Exploramos el impacto de la música en los videojuegos clásicos"
]


def contarPalabras(desc):
    musica = 0
    charla = 0
    entretenimiento = 0
    for d in descriptions: #recorro la lista
        if "música" in d.lower(): #recorro cada descripcion buscando palabras
            musica +=1
        if "charla " in d.lower(): #NOTA PARA MI:poner el espacio en blanco despues de charla si no me incluye charlar
            charla += 1
        if "entretenimiento" in d.lower():#NOTA PARA MI: TENGO QUE USAR LOWER si no cuenta mal
            entretenimiento +=1
    return f'Menciones de música: {musica} \nMenciones de charla: {charla} \nMenciones de entretenimiento: {entretenimiento}'

print(contarPalabras(descriptions))