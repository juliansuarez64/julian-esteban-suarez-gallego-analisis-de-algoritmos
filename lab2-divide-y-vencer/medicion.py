"""Medicion de tiempo de ejecucion de los algoritmos de subarreglo maximo."""
import time
import random
import matplotlib.pyplot as plt
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

def main():
    tamanos = [10, 50, 100, 500, 1000, 4000, 8000]
    tiempos_fb = []
    tiempos_dv = []
    
    random.seed(42)
    
    for n in tamanos:
        valores = [random.randint(-100, 100) for _ in range(n)]
        
        start = time.perf_counter()
        _, _, suma_fb = subarreglo_fuerza_bruta(valores)
        end = time.perf_counter()
        tiempos_fb.append(end - start)
        
        start = time.perf_counter()
        _, _, suma_dv = subarreglo_maximo(valores, 0, n - 1)
        end = time.perf_counter()
        tiempos_dv.append(end - start)
        
        assert suma_fb == suma_dv, f"Error en tamano {n}: {suma_fb} != {suma_dv}"
        
        print(f"n={n}: FB={tiempos_fb[-1]:.4f}s, DV={tiempos_dv[-1]:.4f}s")
        
    plt.figure()
    plt.plot(tamanos, tiempos_fb, label="Fuerza Bruta", marker="o")
    plt.plot(tamanos, tiempos_dv, label="Divide y Vencerás", marker="s")
    plt.title("Tiempo de ejecución: Fuerza Bruta vs Divide y Vencerás")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/tiempo_vs_n.png")
    
if __name__ == "__main__":
    main()

