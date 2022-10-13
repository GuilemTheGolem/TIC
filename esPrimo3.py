''' Escriba un algoritmo que proporcione los números primos comprendidos
 entre 1 y 1000. Recuerde que un número primo solo es divisible entre sí
 mismo y por la unidad. Preste atención, lo más sencillo no siempre es lo
 más rápido. '''

def primeros1000primos():
    lst = []
    for i in range(1,1001):
        if(esPrimo(i)):
            lst.append(i)
        
    return lst
print(len(primeros1000primos()))
