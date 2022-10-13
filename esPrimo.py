# ver todos los números primos
def esPrimo(num):
   for i in range (2, num):
    if(num % i == 0):
        return False
    return True
        
n = int(input(("Dime un número:")))
print(esPrimo(n))         



