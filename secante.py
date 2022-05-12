'''
*******************
Método das Secantes
Nome | Julia Lopes da Rocha 
DRE  | 119137336

********************
'''

import math

def f(x):
    y = (x * math.log10(x)) - 1
    return y

def secante(a,b):
    return (f(b)-f(a))/b-a

def raiz(a, b, error):
    iteracoes = 0
    
    medio = a
    while(math.fabs(f(medio) <= error)):   
        medio = b - (f(b)*(b-a)/(f(b)-f(a)))

        a = b
        b = medio

        iteracoes+=1
    
    print(f'Raiz aproximada é {medio}')
    print(f'Número de iteraçoẽs: {iteracoes}')

#definir um intervalo [a,b] e um erro e
raiz(2, 3, math.pow(10,-7))

'''
Algortimo Método das Secantes

ERROR = Erro máximo
ITE = Número máximo de Iterações

Entrada: Intervalo [a,b] que contém a raiz 
    X0 = a
    X1 = b

PASSO   1: i = 1
PASSO   2: Enquanto (i < ITE ou f(Xn) > ERROR):
            FAZER PASSOS 3 E 4
PASSO   3: Xn+1 = Xn - Xn-1 * f(Xn) / (f(Xn) - f(Xn-1)) 
PASSO   4: i = i + 1

PASSO 5: SAIDA ("A raíz é: ", Xn)

'''