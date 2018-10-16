def inlezen_beginstation(stations):
    beginstation = input('Welk station is het begin station? ')
    while beginstation not in stations:
        beginstation = input('Deze invoer komt niet voor op deze lijn. Welk station is het begin station? ')
    return beginstation

def inlezen_eindstation(stations, beginstation):
    eindstation = input('Welk station is het eind station? ')
    while eindstation not in stations:
        eindstation = input('Deze invoer komt niet voor op deze lijn. Welk station is het eind station? ')
    while stations.index(eindstation) <= stations.index(beginstation):
        eindstation = input('Deze invoer komt niet voor op deze lijn. Welk station is het eind station? ')
    return eindstation

def omroepen_reis(stations, beginstation, eindstation):
    beginstation_index = stations.index(beginstation)+1
    eindstation_index = stations.index(eindstation)+1
    verschil = eindstation_index - beginstation_index
    prijs = verschil*5
    tussenstations = ""
    print("de reis begint in {}, dit is het {}e station op de lijn".format(beginstation, beginstation_index))
    print("De reis is klaar in {}, dit is het {}e station op de lijn".format(eindstation, eindstation_index))
    print("de afstand is {} stations".format(verschil))
    print("je ritprijs is {} euro".format(prijs))
    for i in range(beginstation_index, eindstation_index):
        tussenstations += stations[i] + "\n "
    print("je reis begint in {} en je tussnestations zijn {} je eindigt in {}".format(beginstation, tussenstations, eindstation))

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)