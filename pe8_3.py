invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
invoer = invoer.split("-")
invoer.sort()
int_invoer = []
for item in invoer:
    item = int(item)
    int_invoer.append(item)
print("Gesorteerde list van ints: {}".format(int_invoer))
print("Grootste getal: {} en Kleinste getal: {}".format(max(int_invoer), min(int_invoer)))
print("Aantal getallen: {} en Som van de getallen: {}".format(len(int_invoer), sum(int_invoer)))
print("Gemiddelde: {}".format(sum(int_invoer)/len(int_invoer)))