"""Generadores de lotes de registros para los escenarios de Tamiza."""
import random

def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    random.seed(semilla)
    datos = list(range(1000000, 1000000 + n))
    random.shuffle(datos)
    return datos

def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    random.seed(semilla)
    n_ordenado = int(n * 0.98)
    n_desordenado = n - n_ordenado
    
    base_datos = list(range(1000000 + n, 1000000, -1))
    ordenado = base_datos[:n_ordenado]
    desordenado = base_datos[n_ordenado:]
    random.shuffle(desordenado)
    
    return ordenado + desordenado

def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    return list(range(1000000, 1000000 + n))

