file = open('Kaartnummers.txt','r')

grootste_nummer = 0
regel_grootste_nummer = 0
regelnummer = 0
for line in file.readlines():
    regelnummer +=1
    nummer_enz = line.split(", ")
    nummer = int(nummer_enz[0])
    if grootste_nummer < nummer:
        grootste_nummer = nummer
        regel_grootste_nummer = regelnummer

print("Deze file telt {} regels".format(regelnummer))
print("Het grootste kaartnummer is: {} en dat staat op regel {}".format(grootste_nummer, regel_grootste_nummer))