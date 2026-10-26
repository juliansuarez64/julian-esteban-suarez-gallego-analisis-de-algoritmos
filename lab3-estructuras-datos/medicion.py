"""Medicion experimental y generacion de graficas para ListaEnlazada y TablaHash."""

from __future__ import annotations

import os
import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


def es_primo(numero: int) -> bool:
    """Determina si un numero entero es primo.

    Args:
        numero: numero a evaluar.

    Returns:
        True si el numero es primo, False de lo contrario.
    """
    if numero < 2:
        return False
    if numero in (2, 3):
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True


def siguiente_primo(inicio: int) -> int:
    """Encuentra el menor numero primo mayor o igual a inicio.

    Args:
        inicio: valor a partir del cual buscar.

    Returns:
        Numero primo mayor o igual que inicio.
    """
    candidato = max(2, inicio)
    while not es_primo(candidato):
        candidato += 1
    return candidato


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_guias_existentes(n: int, semilla: int = 42) -> list[int]:
    """Genera n guias unicas de diez digitos.

    Args:
        n: cantidad de guias a generar.
        semilla: semilla para reproducibilidad.

    Returns:
        Lista de n enteros unicos de diez digitos.
    """
    azar = random.Random(semilla)
    guias: set[int] = set()
    while len(guias) < n:
        guias.add(azar.randint(10**9, 10**10 - 1))
    return list(guias)


def experimento_a(directorio_graficas: Path) -> dict[str, list]:
    """Ejecuta el Experimento A: Comparacion de ListaEnlazada frente a TablaHash.

    Mide el tiempo medio de busqueda de guias inexistentes para seis valores de n.
    Para cada n se ejecutan 200 busquedas por ronda durante 5 repeticiones,
    tomando el menor tiempo medio para filtrar ruido e interrupciones del SO.
    Genera la grafica graficas/lista_vs_tabla.png.

    Args:
        directorio_graficas: ruta al directorio donde se guardara la grafica.

    Returns:
        Diccionario con los resultados medidos.
    """
    print("\n--- Ejecutando Experimento A: ListaEnlazada vs. TablaHash ---")
    valores_n = [100, 500, 1000, 5000, 20000, 50000]
    num_busquedas = 200
    num_repeticiones = 5

    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []
    m_usados: list[int] = []
    alfas_obtenidos: list[float] = []

    for n in valores_n:
        m = siguiente_primo(max(3, n // 2))
        m_usados.append(m)

        guias = generar_guias_existentes(n, semilla=42 + n)
        set_guias = set(guias)

        lista = ListaEnlazada()
        tabla = TablaHash(m)

        for guia in guias:
            lista.insertar(guia, "en bodega")
            tabla.insertar(guia, "en bodega")

        alfas_obtenidos.append(tabla.factor_carga())

        # Verificacion interna de consistencia en una muestra
        muestra = guias[: min(50, n)]
        for guia in muestra:
            assert lista.buscar(guia) == "en bodega"
            assert tabla.buscar(guia) == "en bodega"
            assert lista.buscar(guia) == tabla.buscar(guia)

        # Generar guias inexistentes fijas
        inexistentes = generar_guias_inexistentes(
            set_guias, cantidad=num_busquedas, semilla=7
        )

        # Medir lista enlazada (5 repeticiones de las 200 busquedas, tomando el minimo)
        tiempos_rep_lista: list[float] = []
        for _ in range(num_repeticiones):
            t0 = time.perf_counter()
            for guia_inex in inexistentes:
                lista.buscar(guia_inex)
            t1 = time.perf_counter()
            tiempos_rep_lista.append((t1 - t0) / num_busquedas)
        tiempo_medio_lista = min(tiempos_rep_lista)
        tiempos_lista.append(tiempo_medio_lista)

        # Medir tabla hash (5 repeticiones de las 200 busquedas, tomando el minimo)
        tiempos_rep_tabla: list[float] = []
        for _ in range(num_repeticiones):
            t0 = time.perf_counter()
            for guia_inex in inexistentes:
                tabla.buscar(guia_inex)
            t1 = time.perf_counter()
            tiempos_rep_tabla.append((t1 - t0) / num_busquedas)
        tiempo_medio_tabla = min(tiempos_rep_tabla)
        tiempos_tabla.append(tiempo_medio_tabla)

        print(
            f"n={n:5d} | m={m:5d} | alpha={tabla.factor_carga():.2f} | "
            f"T. Lista: {tiempo_medio_lista * 1e3:8.4f} ms | "
            f"T. Tabla: {tiempo_medio_tabla * 1e6:8.3f} us"
        )

    # Grafica Experimento A con ambas curvas en los mismos ejes
    plt.figure(figsize=(9, 5.5))
    plt.plot(
        valores_n,
        tiempos_lista,
        marker="o",
        linewidth=2.2,
        color="#d9534f",
        label=r"Lista Enlazada [$\Theta(n)$]",
    )
    plt.plot(
        valores_n,
        tiempos_tabla,
        marker="s",
        linewidth=2.2,
        color="#0275d8",
        label=r"Tabla Hash ($\alpha \approx 2$) [$\Theta(1 + \alpha)$]",
    )

    plt.title(
        "Tiempo medio de búsqueda de guías inexistentes vs. Número de guías (n)",
        fontsize=12,
        fontweight="bold",
        pad=12,
    )
    plt.xlabel("Número de guías (n)", fontsize=11)
    plt.ylabel("Tiempo medio por búsqueda (segundos)", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=11, loc="upper left")
    plt.tight_layout()

    ruta_grafica_a = directorio_graficas / "lista_vs_tabla.png"
    plt.savefig(ruta_grafica_a, dpi=300)
    plt.close()
    print(f"Grafica guardada en: {ruta_grafica_a}")

    return {
        "n": valores_n,
        "m": m_usados,
        "alpha": alfas_obtenidos,
        "tiempos_lista": tiempos_lista,
        "tiempos_tabla": tiempos_tabla,
    }


def experimento_b(directorio_graficas: Path) -> dict[str, list]:
    """Ejecuta el Experimento B: Efecto del factor de carga (alpha) en TablaHash.

    Con n fijo en 20.000 guias, varia m para evaluar diferentes valores de alpha.
    Para cada configuracion se ejecutan 200 busquedas inexistentes en 5 repeticiones,
    tomando el menor tiempo medio para garantizar estabilidad.
    Genera la grafica graficas/tiempo_vs_alfa.png.

    Args:
        directorio_graficas: ruta al directorio donde se guardara la grafica.

    Returns:
        Diccionario con los resultados medidos.
    """
    print("\n--- Ejecutando Experimento B: Efecto del factor de carga (alpha) ---")
    n_fijo = 20000
    num_busquedas = 200
    num_repeticiones = 5

    # Valores objetivos de alpha entre 0.25 y 10
    alfas_objetivo = [0.5, 1.0, 2.0, 4.0, 6.0, 8.0, 10.0]
    tiempos_tabla: list[float] = []
    alfas_reales: list[float] = []
    m_usados: list[int] = []

    guias = generar_guias_existentes(n_fijo, semilla=999)
    set_guias = set(guias)
    inexistentes = generar_guias_inexistentes(
        set_guias, cantidad=num_busquedas, semilla=7
    )

    for alpha_obj in alfas_objetivo:
        m_estimado = int(round(n_fijo / alpha_obj))
        m = siguiente_primo(m_estimado)
        m_usados.append(m)

        tabla = TablaHash(m)
        for guia in guias:
            tabla.insertar(guia, "en bodega")

        alpha_real = tabla.factor_carga()
        alfas_reales.append(alpha_real)

        # Repeticiones para mitigar ruido en tiempos de sub-microsegundos
        tiempos_rep: list[float] = []
        for _ in range(num_repeticiones):
            t0 = time.perf_counter()
            for guia_inex in inexistentes:
                tabla.buscar(guia_inex)
            t1 = time.perf_counter()
            tiempos_rep.append((t1 - t0) / num_busquedas)

        tiempo_medio = min(tiempos_rep)
        tiempos_tabla.append(tiempo_medio)

        print(
            f"alpha_obj={alpha_obj:4.1f} | m={m:5d} | alpha_real={alpha_real:5.3f} | "
            f"Tiempo medio: {tiempo_medio * 1e6:7.3f} us ({tiempo_medio:10.8f} s)"
        )

    # Grafica Experimento B
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(
        alfas_reales,
        tiempos_tabla,
        marker="o",
        linewidth=2.2,
        color="#2e7d32",
        label=f"Tabla Hash (n = {n_fijo} guías)",
    )
    ax.set_title(
        f"Tiempo medio de búsqueda infructuosa vs. Factor de carga (α) [n = {n_fijo}]",
        fontsize=12,
        fontweight="bold",
        pad=12,
    )
    ax.set_xlabel(r"Factor de carga ($\alpha = n / m$)", fontsize=11)
    ax.set_ylabel("Tiempo medio por búsqueda (segundos)", fontsize=11)
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(fontsize=11, loc="upper left")
    fig.tight_layout()

    ruta_grafica_b = directorio_graficas / "tiempo_vs_alfa.png"
    fig.savefig(ruta_grafica_b, dpi=300)
    plt.close(fig)
    print(f"Grafica guardada en: {ruta_grafica_b}")

    return {
        "alpha_obj": alfas_objetivo,
        "m": m_usados,
        "alpha_real": alfas_reales,
        "tiempos_tabla": tiempos_tabla,
    }


def main() -> None:
    """Coordina la ejecucion de los experimentos y la generacion de graficas."""
    directorio_base = Path(__file__).resolve().parent
    directorio_graficas = directorio_base / "graficas"
    directorio_graficas.mkdir(parents=True, exist_ok=True)

    res_a = experimento_a(directorio_graficas)
    res_b = experimento_b(directorio_graficas)

    print("\nMediciones y graficas generadas exitosamente.")


if __name__ == "__main__":
    main()
