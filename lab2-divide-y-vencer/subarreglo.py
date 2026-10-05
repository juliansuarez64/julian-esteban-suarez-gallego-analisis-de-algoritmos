"""Subarreglo maximo: fuerza bruta y divide y venceras."""

def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).

    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    n = len(valores)
    mejor_suma = float("-inf")
    mejor_inicio = -1
    mejor_fin = -1

    for i in range(n):
        suma_actual = 0.0
        for j in range(i, n):
            suma_actual += valores[j]
            if suma_actual > mejor_suma:
                mejor_suma = suma_actual
                mejor_inicio = i
                mejor_fin = j
                
    return mejor_inicio, mejor_fin, float(mejor_suma)

def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    suma_izq = float("-inf")
    suma_actual = 0.0
    mejor_izq = medio
    for i in range(medio, inicio - 1, -1):
        suma_actual += valores[i]
        if suma_actual > suma_izq:
            suma_izq = suma_actual
            mejor_izq = i
            
    suma_der = float("-inf")
    suma_actual = 0.0
    mejor_der = medio + 1
    for j in range(medio + 1, fin + 1):
        suma_actual += valores[j]
        if suma_actual > suma_der:
            suma_der = suma_actual
            mejor_der = j
            
    return mejor_izq, mejor_der, float(suma_izq + suma_der)

def subarreglo_maximo(
    valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar (inclusive).
        fin: indice final del rango a considerar (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    if inicio == fin:
        return inicio, fin, float(valores[inicio])
        
    medio = (inicio + fin) // 2
    
    izq_ini, izq_fin, izq_suma = subarreglo_maximo(valores, inicio, medio)
    der_ini, der_fin, der_suma = subarreglo_maximo(valores, medio + 1, fin)
    cruz_ini, cruz_fin, cruz_suma = suma_cruzada(valores, inicio, medio, fin)
    
    if izq_suma >= der_suma and izq_suma >= cruz_suma:
        return izq_ini, izq_fin, izq_suma
    elif der_suma >= izq_suma and der_suma >= cruz_suma:
        return der_ini, der_fin, der_suma
    else:
        return cruz_ini, cruz_fin, cruz_suma

