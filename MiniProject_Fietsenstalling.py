import csv

def alle_informatie():

    with open('fietsenstalling.CSV', 'r') as myCSVFile:

        reader = csv.reader(myCSVFile, delimiter=';')

        for row in reader:
            print('Naam: {}, Geboortedatum: {}, Geslacht: {}, Nummervandefiets: {}'.format(row[0], row[1], row[2], row[3]))

def schrijven_naar_CSV():
    with open('fietsenstalling.CSV', 'a', newline = '') as myCSVFile:
        writer = csv.writer(myCSVFile, delimiter=';')

        name = str(input('Name? '))
        geboortedatum = str(input('geboortedatum? '))
        geslacht = str(input('M/V? '))
        nummervandefiets = str('0000000000')
        writer.writerow((name, geboortedatum, geslacht, nummervandefiets))

schrijven_naar_CSV()
