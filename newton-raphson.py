import math

def f(x):
    y = x * math.log10(x) - 1
    return y

#Cálculo da derivada de uma função
def derivada(x):
    h = 1e-8
    d_result = (f(x+h) - f(x))/h
    return d_result

def mnr(x, error):

    iteracoes = 0

    while(math.fabs(f(x))>error):
        x = x - (f(x)/derivada(x))
        iteracoes+=1

    print(f'Raiz aproximada é {x}')
    print(f'Número de iteraçoẽs: {iteracoes}')

#definir um intervalo [a,b] e um erro e
mnr(2, math.pow(10,-7))