rounds = [
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
        'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
        'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
        'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
        'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
    }
]

#a partir del diccionario proporcionado voy a tener que crear un nuevo diccionario con los puntajes
#creo mi nuevo diccionario donde almaceno kill ass y d(los puntajes totales)
scores = {} 
mvp = {} #creo otro diccionario para mvps


for round_number, r in enumerate(rounds, start = 1): #por cada ronda. Al principio habia usado una variable i para incrementar el numero de ronda pero asi me ahorro tener q usar una variable extra
    
    #para guardarme el puntaje de la ronda de c/jugador:
    round_scores = {}                   
    print('-'*100)
    print(f'Resultados de la ronda {round_number} :')
    print('-'*100)
    
    #a partir de aca registro los puntajes de la ronda: 
    for player, valor in r.items():         #por cada clave:valor de la ronda:
        if player not in scores:            #inicializo cada puntaje del jugador en 0 en el nuevo diccionario scores
            scores[player] = {'kills':0, 'assists':0, 'deaths':0, 'points':0}
            round_scores[player] = {'kills':0, 'assists':0, 'deaths':0, 'points':0}
            mvp[player] = 0                 #el diccionario de mvp tambien lo inicializo en 0
        score_round =(                    #calculo el score que saco en esa ronda:
            (valor['kills'] * 3) + #de la parte valor del diccionario en la posicion 'kill', multiplico el valor de lo que encuetre ahi por los puntos correspondientes
            (valor['assists'] * 1) +
            (-1 if valor['deaths'] else 0)# tengo que checkear t o f porque es boolean asignarle el puntaje
        )

        #le asigno el puntaje de la ronda a las estadisticas del jugador
        # a mi nuevo diccionario le asigno la suma de puntos en la posición del jugador actual, se van acumulando los puntos.
        scores[player]['kills'] += valor['kills'] 
        scores[player]['assists'] += valor['assists'] 
        scores[player]['deaths'] += int(valor['deaths'])    #convierto el boolean a int
        scores[player]['points'] += score_round

        #me guardo en el diccionario score rounds solo los puntos de esta ronda
        round_scores[player] = {
            'kills': valor['kills'],
            'assists': valor['assists'],
            'deaths': int(valor['deaths']),
            'points': score_round
        }
    #organizo la tabla de mayor a menor
    sorted_round = sorted(round_scores.items(), key=lambda x: x[1]['points'], reverse=True)

    #imprimo la tabla ORDENADA
    for player, score in sorted_round:
        print(f'nombre: {player} : {score}')
        #print(f'nombre: {player}, {r.values()},\n')        

    #busco al jugador con mayor puntaje de la ronda actual y lo guardo en mvp_ronda
    mvp_ronda = max(round_scores, key=lambda p: round_scores[p]['points'])
    print(f'el mvp de la ronda fue: {mvp_ronda}')
    mvp[mvp_ronda] += 1 #le sumo al jugador correspondiente 1 en la cuenta de veces de mvp
    #
print("-" * 100)
print("Ranking final: ")
print("-" * 100)
#primero ordeno la tabla de mayores puntos a menores
sorted_scores = sorted(scores.items(), key=lambda x: x[1]['points'], reverse=True)
for player, score in sorted_scores:
    print(f"{player}: {score} puntos. MVPs: {mvp[player]}")
