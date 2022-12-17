#main.py
from operadores import sumar_numeros
from operadores import restar_numeros
from operadores import potencia
from operadores import cos
from operadores import sen
from operadores import tan
from operadores import csc
from operadores import sec
from operadores import cot 
from operadores import ln 
from operadores import exp
from operadores import multiplicar_numeros
from operadores import division


def main():
    print_menu() 
    option = int(input('ingresar opcion: '))
    
    if option == 1:
        x = int(input('numero x: '))
        y = int(input('numero y: '))
        output = sumar_numeros(x, y) 
        print('el resultado es: ', output) 
    elif option == 2:
        x = int(input('numero x: '))
        y = int(input('numero y: '))
        output = restar_numeros(x, y)
        print('el resultado es: ', output) 
    elif option == 3:
        x = int(input('numero x: '))
        n = int(input('numero n: '))
        output = potencia(x, n)
        print('el resultado es: ', output) 
    elif option == 4:
        x = int(input('numero x: '))
        output = cos(x)
        print('el resultado es: ', output)
    elif option == 5:
        x = int(input('numero x: '))
        output = sen(x)
        print('el resultado es: ', output)  
    elif option == 6:
        x = int(input('numero x: '))
        output = tan(x)
        print('el resultado es: ', output)   
    elif option == 7:
        x = int(input('numero x: '))
        output = csc(x)
        print('el resultado es: ', output)   
    elif option == 8:
        x = int(input('numero x: '))
        output = sec(x)
        print('el resultado es: ', output)
    elif option == 9:
        x = int(input('numero x: '))
        output = cot(x)
        print('el resultado es: ', output)
    elif option == 10:
        x = int(input('numero x: '))
        output = ln(x)
        print('el resultado es: ', output)
    elif option == 11:
        x = int(input('numero x: '))
        output = exp(x)
        print('el resultado es: ', output)
    elif option == 12:
        x = int(input('numero x: '))
        y = int(input('numero y: '))
        output = multiplicar_numeros(x, y)
        print('el resultado es: ', output) 
    elif option == 13:
        x = int(input('numero x: '))
        y = int(input('numero y: '))
        output = division(x, y)
        print('el resultado es: ', output) 
    else:
        print('operador no valido, finalizado')

    
def print_menu():
    print('elije el operador a realizar: ')
    print('')
    print('1 suma de dos numeros')
    print('2 resta de dos numeros')
    print('3 potencia')
    print('4 cos')
    print('5 sen')
    print('6 tan')
    print('7 csc')
    print('8 sec')
    print('9 cot')
    print('10 In')
    print('11 exp')
    print('12 multiplicacion')
    print('13 division')
    

if __name__ == '__main__':
    main()

