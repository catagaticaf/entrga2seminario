#import this
zen_text =""""The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those! """

for linea in zen_text.split("\n"):#primero separo el texto por linea
    palabras = linea.split() #separo todas las palabras de la linea
    if palabras[1][0].lower() in "aeiou": #checkeo si la segunda palabra empieza con 0
        print(linea)                         #lo paso todo a vocal pra que la comparacion con las vocales sea mas facil
