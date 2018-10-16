wachtwoord=input('Voer een wachtwoord in: ')
while True:
    if len(wachtwoord) == 4:
        break
    else:
        print('{} heeft {} letters'.format(wachtwoord, len(wachtwoord)))
        wachtwoord = input('Voer een wachtwoord in: ')
print('Inlezen van correcte string: {} is geslaagd'.format(wachtwoord))