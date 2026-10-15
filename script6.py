import time
import matplotlib.pyplot as plt

def suma_objetivo(lista, objetivo):
    n = len(lista)
    for i in range (n):
        for j in range (i + 1, n):
            if lista[i] + lista[j] == objetivo:
                return True
    return False

if __name__ == '__main__':
    tamanos = [1000, 2000, 4000, 6000, 8000, 10000 ]

    objetivo_imposible = -1
    tiempos_reales = []

    print(" midiendo tiempos reales en ejecucion")

    for n in tamanos:
        lista_prueba = [i for i in range (n)]

        inicio = time.perf_counter()
        suma_objetivo(lista_prueba, objetivo_imposible)
        final = time.perf_counter()

        tiempo = final - inicio
        tiempos_reales.append(tiempo)

        print(f"tiempo para n = {n:10d} -> tiempo: {tiempo:.6f} segundos")

    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_reales, marker='o', color='red', linestyle='-')
    plt.xlabel('Tamaño de la lista (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('complejidad de suma_objetivo - O(n^2)')
    plt.grid(True)
    plt.show()

