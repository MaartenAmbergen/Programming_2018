cijferICOR=8.0
cijferPROG=8.3
cijferCSN=8.5
gemiddelde=(cijferICOR+cijferPROG+cijferCSN)/3
beloning=gemiddelde*30.0
overzicht='Mijn cijfers (gemiddeld een '+ str(round(gemiddelde, 1)) + ') leveren een beloning van €' + str(round(beloning,1)) +' op!'

print(overzicht)