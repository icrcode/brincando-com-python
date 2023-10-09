print("Funcao recursiva para o calculo de numeros de fibonacci.")

def fib_python(n):
    if n == 0 or n == 1:
        return n
    return fib_python(n-1) + fib_python( n - 2)

print(fib_python(35))