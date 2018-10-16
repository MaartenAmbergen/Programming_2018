getallen = []
while True:
    getal = int(input('geef een getal op: '))
    if getal == 0:
        break
    else:
        getallen.append(getal)

som=sum(getallen)
print('er zijn {} getallen ingevoer, de som van deze getallen is {}!'.format(len(getallen), som))