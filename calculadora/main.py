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


valid_operators = {
    1: sumar_numeros,
    2: restar_numeros,
    3: multiplicar_numeros,
    4: division,
    5: potencia,
    6: cos,
    7: sen,
    8: tan,
    9: csc,
    10: sec,
    11: cot,
    12: ln,
    13: exp
}

def main():
    print_menu() 
    option = int(input('ingresar opcion: '))
    if option in valid_operators.keys():
        compute_operator(option)
    else:
        print('Operador no valido. Finalizacion de programa')


def compute_operator(option):
    if option <= 5:
        x = int(input('numero x: '))
        y = int(input('numero y: '))
        output = valid_operators[option](x, y)
    else:
         x = int(input('numero x: '))
         output = valid_operators[option](x)
    print('el resultado es: ', output)


def print_menu():
    print('elije el operador a realizar: ')
    for key, val in valid_operators.items():
        print(f'{key} : {val.__name__} ')

    

if __name__ == '__main__':
    main()

