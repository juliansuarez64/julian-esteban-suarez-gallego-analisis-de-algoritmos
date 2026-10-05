import time
import matplotlib.pyplot as plt
import os
from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

def main():
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]
    
    comparaciones_a = []
    comparaciones_b = []
    comparaciones_c = []
    
    tiempos_a = []
    tiempos_b = []
    tiempos_c = []
    
    for n in tamanos:
        datos_a = generar_aleatorio(n)
        start = time.perf_counter()
        _, comp_a = insertion_sort(datos_a)
        end = time.perf_counter()
        tiempos_a.append(end - start)
        comparaciones_a.append(comp_a)
        
        datos_b = generar_casi_ordenado(n)
        start = time.perf_counter()
        _, comp_b = insertion_sort(datos_b)
        end = time.perf_counter()
        tiempos_b.append(end - start)
        comparaciones_b.append(comp_b)
        
        datos_c = generar_inverso(n)
        start = time.perf_counter()
        _, comp_c = insertion_sort(datos_c)
        end = time.perf_counter()
        tiempos_c.append(end - start)
        comparaciones_c.append(comp_c)
        
    os.makedirs("graficas", exist_ok=True)
    
    plt.figure()
    plt.plot(tamanos, comparaciones_a, label="Escenario A (Aleatorio)", marker="o")
    plt.plot(tamanos, comparaciones_b, label="Escenario B (Casi Ordenado)", marker="s")
    plt.plot(tamanos, comparaciones_c, label="Escenario C (Inverso)", marker="^")
    plt.title("Insertion Sort: Comparaciones vs Tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/parte3_comparaciones.png")
    
    plt.figure()
    plt.plot(tamanos, tiempos_a, label="Escenario A (Aleatorio)", marker="o")
    plt.plot(tamanos, tiempos_b, label="Escenario B (Casi Ordenado)", marker="s")
    plt.plot(tamanos, tiempos_c, label="Escenario C (Inverso)", marker="^")
    plt.title("Insertion Sort: Tiempo de ejecución vs Tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/parte3_tiempo.png")

if __name__ == "__main__":
    main()

