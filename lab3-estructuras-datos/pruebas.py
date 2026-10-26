"""Pruebas de correctitud para ListaEnlazada y TablaHash."""

import random
from estructuras import ListaEnlazada, TablaHash


def probar_lista_enlazada() -> None:
    """Verifica operaciones basicas de busqueda e insercion en ListaEnlazada."""
    lista = ListaEnlazada()
    assert lista.tamano == 0
    assert lista.cabeza is None
    assert lista.buscar(1000000001) is None

    lista.insertar(1000000010, "en bodega")
    lista.insertar(1000000024, "en reparto")
    lista.insertar(1000000005, "entregado")

    assert lista.tamano == 3
    # Busquedas exitosas
    assert lista.buscar(1000000010) == "en bodega"
    assert lista.buscar(1000000024) == "en reparto"
    assert lista.buscar(1000000005) == "entregado"

    # Busquedas infructuosas
    assert lista.buscar(9999999999) is None
    assert lista.buscar(1000000017) is None


def probar_colision_forzada() -> None:
    """Verifica el manejo de colisiones forzadas en TablaHash con m = 7."""
    m = 7
    tabla = TablaHash(m)

    # Las guias 10, 24 y 17 tienen residuo 3 modulo 7
    guias_colision = (10, 24, 17)
    for guia in guias_colision:
        assert tabla.hash(guia) == 3

    for guia in guias_colision:
        tabla.insertar(guia, "en bodega")

    # Verificar que las tres guias estan en la casilla 3 y su lista mide 3
    assert tabla.casillas[3].tamano == 3
    assert tabla.tamano == 3

    # Las demas casillas deben estar vacias
    for i in range(m):
        if i != 3:
            assert tabla.casillas[i].tamano == 0

    # Busquedas exitosas de las guias colisionadas
    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en bodega"
    assert tabla.buscar(17) == "en bodega"

    # Busqueda infructuosa (clave inexistente en casilla vacia e inexistente en casilla con elementos)
    assert tabla.buscar(99) is None  # 99 % 7 = 1 (casilla vacia)
    assert tabla.buscar(31) is None  # 31 % 7 = 3 (misma casilla pero no insertada)

    # Factor de carga
    assert tabla.factor_carga() == 3 / 7


def probar_colecciones_aleatorias(num_colecciones: int = 25) -> None:
    """Verifica que lista y tabla devuelven exactamente lo mismo en colecciones aleatorias.

    Args:
        num_colecciones: cantidad de colecciones aleatorias a evaluar (minimo 20).
    """
    estados = ["en bodega", "en reparto", "entregado", "devuelto", "en transito"]
    azar = random.Random(12345)

    for i in range(num_colecciones):
        n_elementos = azar.randint(30, 250)
        # m primo para dispersar
        m = azar.choice([17, 31, 53, 97, 127])

        lista = ListaEnlazada()
        tabla = TablaHash(m)

        datos: dict[int, str] = {}
        while len(datos) < n_elementos:
            guia = azar.randint(10**9, 10**10 - 1)
            if guia not in datos:
                estado = azar.choice(estados)
                datos[guia] = estado
                lista.insertar(guia, estado)
                tabla.insertar(guia, estado)

        assert lista.tamano == n_elementos
        assert tabla.tamano == n_elementos
        assert abs(tabla.factor_carga() - (n_elementos / m)) < 1e-9

        # Probar todas las guias existentes
        for guia, estado_esperado in datos.items():
            res_lista = lista.buscar(guia)
            res_tabla = tabla.buscar(guia)
            assert res_lista == estado_esperado, f"Fallo en lista con guia {guia}"
            assert res_tabla == estado_esperado, f"Fallo en tabla con guia {guia}"
            assert res_lista == res_tabla

        # Probar guias inexistentes
        inexistentes_probadas = 0
        while inexistentes_probadas < 30:
            candidata = azar.randint(10**9, 10**10 - 1)
            if candidata not in datos:
                assert lista.buscar(candidata) is None
                assert tabla.buscar(candidata) is None
                inexistentes_probadas += 1


def main() -> None:
    """Ejecuta toda la suite de pruebas de correctitud."""
    print("Iniciando pruebas unitarias y de correctitud...")
    probar_lista_enlazada()
    print("[OK] Pruebas de ListaEnlazada superadas.")
    probar_colision_forzada()
    print("[OK] Pruebas de colision forzada y factor_carga() superadas.")
    probar_colecciones_aleatorias(25)
    print("[OK] Pruebas de 25 colecciones aleatorias (existentes e inexistentes) superadas.")
    print("Todas las pruebas pasaron satisfactoriamente.")


if __name__ == "__main__":
    main()
