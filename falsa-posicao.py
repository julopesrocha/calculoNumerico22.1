import math

def f(x):
    y = x * math.log10(x) - 1
    return y

# vantagem em relação ao método da bissecao pois privilegia o menor valor no intervalo entre a e b
# diferença forma de atualização da raiz 
def falsaPos(a, b, error): 
    err = math.fabs(b-a)/2
    iteracoes = 0

    # Teorema de Bolzano(verif se há uma raiz no intervalo)]
    if f(a)*f(b) < 0:
        
        while(err > error):
            iteracoes+=1
            medio = (a*f(b) - b*f(a)) / (f(b) - f(a)) 

            if f(medio) == 0:
                print(f"A raiz é: {medio}")
                break
            else:
                if (f(a) * f(medio)) < 0:
                    b = medio
                else:
                    a = medio 
        if err <= error:
            print(f'A raiz aproximada da função f será {medio} com f(x) = {f(medio)}. Com {err}<={error}')
        print(f'A raiz aproximada da função f será {medio} com f(x) = {f(medio)}. Com erro: {err} >= {error}')
    else:
        print("Não há raiz nesse intervalo") 
    print(f'Número de iteraçoẽs: {iteracoes}')

#definir um intervalo [a,b] e um erro e
falsaPos(2, 3, math.pow(10,-7))