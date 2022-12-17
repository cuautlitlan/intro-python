#operadores.py 
import math
from constantes import e

def sumar_numeros(x, y):
    return x + y 


def restar_numeros(x, y):
    return x - y 


def multiplicar_numeros(x, y):
    return x * y 


def potencia(x, n): 
    return x ** n 


def raiz(x, n):
    return x ** (1 / n)


def cos(x): 
    return math.cos(x)


def sen(x): 
    return math.sin(x)


def csc(x):
    return 1 / sen(x)


def sec(x): 
    return 1 / cos(x)


def tan(x):
    return sen(x) / cos(x)


def cot(x):
    return cos(x) / sen(x) 


def exp(x):
    return e ** x 


def ln(x):
    return math.log(x, e)


if __name__ == '__main__':
    output = csc(5)
    print(output)
