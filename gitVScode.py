print("Hola mundo")

def factorial1(n):
    fac = 1
    for i in range(1,n+1):
         fac = fac*i
    return fac

valor = factorial1(5)
print(str(valor))