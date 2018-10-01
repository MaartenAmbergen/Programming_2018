def gemiddelde():
    zin = input('Voer een zin in: ')
    zin = zin.split(' ')
    lengte = 0
    deelfactor = 0
    for woord in zin:
        print(woord)
        lengte += len(woord)
        deelfactor = deelfactor + 1
    print(float(lengte/deelfactor))




gemiddelde()
