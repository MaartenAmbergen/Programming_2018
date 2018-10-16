def seizoen(maand):
    if maand in(1,2,3,4,5,6,7,8,9,10,11,12):
        if maand in (3, 4, 5):
            print('lente')
        elif maand in (6,7,8):
            print('zomer')
        elif maand in (9, 10, 11):
            print('herfst')
        else:
            print('winter')
    else:
        print('dit is geen maandnummer')

seizoen(int(input('welke maand? ')))