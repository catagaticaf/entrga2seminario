
def cleanData(clients_list):
    cleaned_list = [] #TUVE QUE HACER UNA LISTA NUEVA, porque mientras la recorría iba eliminando elemntos y eso me cambiaba todos los indices
    for c in clients_list:
        if c is not None and c != "" and c != " ": #asi me aseguro que en mi lista nueva solo incluya nombres
            c = c.title() #cambio a mayusculas las primeras letras
            c = c.strip() #le saco los espacios en blanco al principio y al final
            if c not in cleaned_list: #asi no guardo los repetidos
                cleaned_list.append(c)# lo agrego a la lista nueva
    return(cleaned_list)



clients = [
" Ana López ", "Pedro Gómez", "maria martínez", "Pedro Gómez ", "",
" Luis Rodríguez ", None, "ana lópez", "JUAN PÉREZ", "MARTA SUÁREZ",
"luis rodríguez", "maría martínez ", " claudia torres", "CLAUDIA TORRES",
" ", "pedro gómez", "Juan Pérez", None, "Ricardo Fernández", "LAURA RAMOS",
"carlos mendes", "RICARDO FERNÁNDEZ ", " Laura ramos", "CARLOS MENDES",
"alejandro gonzález", " ALEJANDRO GONZÁLEZ ", "Patricia Vega",
"patricia VEGA", "Andrés Ocampo", " andrés ocampo", "Monica Herrera",
"MONICA HERRERA ", "gabriela ruíz", "Gabriela Ruíz", "sandra morales",
"SANDRA MORALES", "miguel ángel", "Miguel Ángel ", " Damián Castillo",
"Damián Castillo ", None, "", " "
]
print("lista vieja: \n", clients)
clientesFacturacion = (cleanData(clients))
print("lista limpia: \n",clientesFacturacion)
