print("Hola mundo")

def factorial1(n):
    
    if n == 0:
        return 1
    elif n < 0:
        mensaje = "No esta definido el factorial para números negativos"
        return mensaje
    else:
        fac = 1
        for i in range(1,n+1):
            fac = fac*i
        return fac

valor = factorial1(1)
print(str(valor))