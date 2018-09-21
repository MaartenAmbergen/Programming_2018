leeftijd=int(input("Hoe oud ben je? "))
paspoort=str(input('Heb je een geldig nederlands paspoort? '))
if leeftijd >= 18 and paspoort == "ja":
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("je mag niet stemmen")