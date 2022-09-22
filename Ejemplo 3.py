# Escriba, usando comparaciones, un algoritmo
# que muestre el estado del agua (hielo, liquido, vapor)
# en función de su temperatura.
tempt = 0
tempt = float(input("Dime la tempt:"))
# Comprobamos los estados
if (tempt < 0):
    print(tempt, " es HIELO")
else:
    if(tempt >= 100):
        print(tempt, " es VAPOR")
    else:
        print(tempt, " es LIQUIDO")

