'''
1. Cree un programa en su lenguaje de programación favorito que use el 
método de Monte Carlo para determinar la probabilidad de cara o escudo
en una moneda justa 

2. Grafique usando una gráfica de línea las iteraciones (eje x) y la probabilidad de de las mismas (eje y).
'''
import random
import matplotlib.pyplot as plt

'''
coin flip  function
0 -> cara
1 -> escudo
'''
def coin_flip():
    return random.randint(0,1)

'''
Simulación de Monte Carlo 
'''
list = []

def monte_carlo(n):
    results = 0
    for i in range(n):
        flip_result = coin_flip()
        results = results + flip_result

        #Calculando el valor de probabilidad
        prob_value = results/(i+1)

        # Agregar los valores de probabilidad a la lista
        list.append(prob_value)

        #Gráfica de línea las iteraciones
        plt.axhline(y=0.5, color='r', linestyle='-')
        plt.xlabel("Iteraciones")
        plt.ylabel('Probabilidad')
        plt.suptitle('100 iteraciones')
        plt.plot(list)

    return results/n

prob = monte_carlo(100)
plt.show()
print('Probabilidad final', prob)