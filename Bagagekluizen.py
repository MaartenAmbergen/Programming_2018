def toon_aantal_kluizen_vrij():
    'deze functie kijkt hoe veel kluizen er al in gebruik zijn en rekent uit hoe veel er nog vrij zijn'
    # Het bestand met kluizen wordt opengemaakt, ingelezen en weer gesloten
    infile = open('kluizen.txt', 'r')
    kluizeninformatie = infile.readlines()
    infile.close()

    totaal_aantal_kluizen = len(kluizeninformatie)    # Elke line is een item in de list, 12-aantal items is hoe veel er nog vrij zijn
    aantal_vrij = 12-totaal_aantal_kluizen

    print(aantal_vrij)

def nieuwe_kluis():
    'deze functie maakt een lijst met getallen die het aantal kluizen voor moeten stellen'
    # Het bestand met kluizen wordt opengemaakt, ingelezen en weer gesloten
    infile = open('kluizen.txt', 'r')
    kluizeninformatie = infile.readlines()
    infile.close()

    kluis_nummers = []   # een lege lijst welke aangevuld kan worden

    for nummer in range(1,13):
        kluis_nummers.append(nummer)

    for kluis in kluizeninformatie:
        gegevensvan1kluis = kluis.split(';')
        string_nummer = gegevensvan1kluis[0]
        nummer = int(string_nummer)
        kluis_nummers.remove(nummer)

    if len(kluis_nummers) > 0:
        nieuw_kluis_nummer = kluis_nummers[0]
        print('Je kluisnummer is {}'.format(nieuw_kluis_nummer))
        wachtwoord=input('Voer een wachtwoord in: ')
        while len(wachtwoord) <4:
            print('Het wachtwoord moet minimaal 4 tekens lang zijn')
            wachtwoord = input('Voer een wachtwoord in: ')
        outfile = open('kluizen.txt', 'a')
        outfile.write('{};{}\n'.format(nieuw_kluis_nummer, wachtwoord))
        outfile.close()

    else:
        print('Er is geen kluis meer beschikbaar')   # Als alle kluizen vol zitten komt dit bericht in beeld


def kluis_openen():
    'deze functie controleert de gegevens van een gebruiker en opent dan een kluis'
    # Het bestand met kluizen wordt opengemaakt, ingelezen en weer gesloten
    infile = open('kluizen.txt', 'r')
    kluizeninformatie = infile.readlines()
    infile.close()

    stringnummer = input('wat is je kluisnummer? ')
    wachtwoord= input('wat is je wachtwoord? ')
    gegevens_correct = False

    for kluis in kluizeninformatie: #Hier wordt gekeken of de ingevoerde gegevens correct zijn
        gegevens_van_1_kluis = kluis.split(';') #alle ingelezen lines worden gesplit op een ;
        string_kluisnummer = gegevens_van_1_kluis[0]
        kluiscode = gegevens_van_1_kluis[1].strip()
        if string_kluisnummer == stringnummer and wachtwoord == kluiscode:
            gegevens_correct = True

    if gegevens_correct: #als de opgegeven gegevens correct zijn wordt de kluis geopend
        print('de kluis is open')

    else: #als de opgegeven gegevens niet correct zijn wordt dit bericht weergegeven (in rode text)
        print("\033[1;31mHet opgegeven wachtwoord of kluisnummer was niet correct!\033[1;m")

# def kluis_teruggeven():
#     'deze functie opent een kluis en haalt daarna de kluis uit de database zodat deze opnieuw kan worden gebruikt'
#    # Het bestand met kluizen wordt opengemaakt, ingelezen en weer gesloten
#     infile = open('kluizen.txt', 'r')
#     kluizeninformatie = infile.readlines()
#     infile.close()
#
#     stringnummer = input('wat is je kluisnummer? ')
#     wachtwoord = input('wat is je wachtwoord? ')
#     gegevens_correct = False
#     index=-1
#
#     for kluis in kluizeninformatie:
#         gegevens_van_1_kluis = kluis.split(';')
#         string_kluisnummer = gegevens_van_1_kluis[0]
#         kluiscode = gegevens_van_1_kluis[1].strip()
#         index += 1
#         if string_kluisnummer == stringnummer and wachtwoord == kluiscode:
#             gegevens_correct = True
#             gegevens_index = index
#
#     if gegevens_correct:
#         print('de kluis is open, haal uw spullen er uit zodat de kluis gereset kan worden')
#
#     else:
#         print('Het opgegeven wachtwoord of kluisnummer was niet correct')
#         return
#
#     print(kluizeninformatie)
#     del kluizeninformatie[gegevens_index]
#     print(str(kluizeninformatie))
#
#     outfile = open('kluizen.txt', 'w')
#     outfile.write(str(kluizeninformatie))
#     outfile.close()

while True:
    print('-------------------------------------------------')
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
    print("2: Ik wil een nieuwe kluis")
    print("3: Ik wil even iets uit mijn kluis halen")
    print("4: Ik geef mijn kluis terug")
    print('5: Programma afsluiten')
    print('-------------------------------------------------')
    keuze = int(input('Maak uw keuze: '))

    if keuze ==1:
        toon_aantal_kluizen_vrij()
    elif keuze ==2:
        nieuwe_kluis()
    elif keuze ==3:
        kluis_openen()
    elif keuze ==4:
        print("\033[1;31mDeze functie is nog niet beschikbaar\033[1;m")
    #     kluis_teruggeven()
    elif keuze ==5:
        break
    else:
        print("\033[1;31mOnbekende Invoer!\033[1;m")