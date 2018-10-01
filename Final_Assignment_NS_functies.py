leeftijd_input = float(input("Hoe oud ben je? "))
dag_van_de_week_input = input("Welke dag is het vandaag? ")
afstandKM_input = float(input("Hoe veel kilometer gaan we vandaag reizen? "))
if dag_van_de_week_input in ["zaterdag", "Zaterdag", "zondag", "Zondag"]:
    weekendrit_input = True
else:
    weekendrit_input = False

def standaardtarief(afstandKM):
    'Bepaalt het standaardbedrag voor een bepaalde rit'
    if afstandKM < 0:
        kosten = 0
    elif afstandKM >50:
        kosten = 15.0+(0.6*afstandKM)
    else:
        kosten = 0.8*afstandKM
    return kosten

def ritprijs(leeftijd, weekendrit, afstandKM):
    'blablabla'
    standaardprijs = standaardtarief(afstandKM)
    if leeftijd <12 or leeftijd >= 65:
        if weekendrit:
            te_betalen_prijs = 0.65*standaardprijs
        else:
            te_betalen_prijs = 0.70*standaardprijs
    else:
        if weekendrit:
            te_betalen_prijs = 0.60*standaardprijs
        else:
            te_betalen_prijs = standaardprijs
    return te_betalen_prijs

print("je gaat vandaag €" +str(round(ritprijs(leeftijd_input, weekendrit_input, afstandKM_input), 2))+ " betalen!")





