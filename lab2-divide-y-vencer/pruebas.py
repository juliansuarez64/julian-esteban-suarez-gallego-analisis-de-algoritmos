"""Pruebas para los algoritmos del subarreglo maximo."""
import random
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

def main():
    # Caso 1: Serie de ejemplo
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(serie)[2] == 17
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17

    # Caso 2: Un solo elemento
    serie = [42]
    assert subarreglo_fuerza_bruta(serie)[2] == 42
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 42

    # Caso 3: Todos negativos
    serie = [-5, -2, -9, -1, -4]
    assert subarreglo_fuerza_bruta(serie)[2] == -1
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == -1

    # Caso 4: Todos positivos
    serie = [1, 2, 3, 4, 5]
    assert subarreglo_fuerza_bruta(serie)[2] == 15
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 15

    # Caso 5: Cruzado
    serie = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert subarreglo_fuerza_bruta(serie)[2] == 6
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 6

    # Caso 6: 20 listas aleatorias
    random.seed(42)
    for _ in range(20):
        n = random.randint(10, 50)
        serie = [random.randint(-100, 100) for _ in range(n)]
        _, _, suma_fb = subarreglo_fuerza_bruta(serie)
        _, _, suma_dv = subarreglo_maximo(serie, 0, len(serie) - 1)
        assert suma_fb == suma_dv

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    main()

