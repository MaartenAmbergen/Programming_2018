lijst = eval(input("Geef lijst met minimaal 10 strings: "))
nieuwe_lijst = []
for item in lijst:
    if len(item) == 4:
        nieuwe_lijst.append(item)
print("De nieuw-gemaakte lijst met alle vier-letter strings is: {}".format(nieuwe_lijst))