def kwadraten_som(grondgetallen):
    antwoord = 0
    for grondgetal in grondgetallen:
        if grondgetal > 0:
            kwadraat=grondgetal**2
            antwoord = antwoord+kwadraat
    print(antwoord)

kwadraten_som([ 4, 5, 3, -81 ])