#importar biblioteca matemática
import math


def func(x):
    y = x * math.log10(x) - 1
    return y

def bissec(a, b, error):
    
    err = math.fabs(b-a)/2

    # Teorema de Bolzano(verif se há uma raiz no intervalo)]
    if func(a)*func(b) < 0:
        
        while(err > error):
            
            medio = (a+b)/2

            if func(medio) == 0:
                print(f"A raiz é: {medio}")
                break
            else:
                if (func(a) * func(medio)) < 0:
                    b = medio
                else:
                    a = medio 
        if err <= error:
            print(f'A raiz aproximada da função f será {medio}. Com {err}<={error}')
        print(f'A raiz aproximada da função f será {medio}. Com erro: {err} >= {error}')
    else:
        print("Não há raiz nesse intervalo") 

#definir um intervalo [a,b] e um erro e
bissec(2, 3, math.pow(10,-7))