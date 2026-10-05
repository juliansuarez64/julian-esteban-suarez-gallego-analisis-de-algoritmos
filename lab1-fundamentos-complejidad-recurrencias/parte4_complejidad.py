import time
import matplotlib.pyplot as plt
import os
from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

def main():
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]
    
    tiempos_insertion = []
    tiempos_merge = []
    
    for n in tamanos:
        datos = generar_aleatorio(n)
        
        start = time.perf_counter()
        insertion_sort(datos)
        end = time.perf_counter()
        tiempos_insertion.append(end - start)
        
        start = time.perf_counter()
        merge_sort(datos)
        end = time.perf_counter()
        tiempos_merge.append(end - start)
        
    os.makedirs("graficas", exist_ok=True)
    
    plt.figure()
    plt.plot(tamanos, tiempos_insertion, label="Insertion Sort", marker="o")
    plt.plot(tamanos, tiempos_merge, label="Merge Sort", marker="s")
    plt.title("Tiempo de ejecución: Insertion Sort vs Merge Sort (Escenario A)")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/parte4_tiempo.png")

if __name__ == "__main__":
    main()

