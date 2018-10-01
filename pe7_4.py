import datetime


while True:
    file = open('hardlopers.txt', 'a')
    naam = input("Naam vd hardloper: ")
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y %H:%M:%S")
    newfile = s + ", " + naam + '\n'
    file.write(newfile)
    file.flush()
    file.close()
print(s, naam)