def convert(Celcius):
    Fahrenheit=Celcius*1.8+32
    return Fahrenheit

def table():
    print('F               C')
    for temperatuur in range(-30, 41, 10):

        print('{:6}{:12}'.format(str(convert(temperatuur)), float(temperatuur)))




table()