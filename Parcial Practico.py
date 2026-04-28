# ============================================================
# SISTEMA DE COMPRA DE BOLETAS - CINE
# ============================================================

# ---------- DATOS DEL SISTEMA -------
GENEROS = ("Acción", "Comedia", "Drama", "Terror", "Animación")

PELICULAS = {
    1: {"titulo": "Super Cool", "genero": GENEROS[1], "duracion": 113, "precio": 12000},
    2: {"titulo": "Proyecto X", "genero": GENEROS[1], "duracion": 88, "precio": 12000},
    3: {"titulo": "John Wick", "genero": GENEROS[0], "duracion": 101, "precio": 15000},
    4: {"titulo": "Spider-Man: No Way Home", "genero": GENEROS[0], "duracion": 148, "precio": 15000},
    5: {"titulo": "Terrifier", "genero": GENEROS[3], "duracion": 85, "precio": 14000},
}

TIPOS_BOLETA = {
    "1": ("General", 1.0),
    "2": ("Estudiante", 0.8),
    "3": ("Adulto Mayor", 0.7),
    "4": ("VIP", 1.5),
}

historial_compras = []

# ===================== FUNCIONES ============================

def mostrar_cartelera():
    print("\n" + "="*55)
    print(" CARTELERA DEL CINE ")
    print("="*55)
    print(f"{'ID':<4} {'TÍTULO':<28} {'GÉNERO':<12} {'PRECIO':>8}")
    print("-"*55)

    for id_pelicula, datos in PELICULAS.items():
        print(f"{id_pelicula:<4} {datos['titulo']:<28} {datos['genero']:<12} ${datos['precio']:>7,}")

    print("="*55)


def mostrar_tipos_boleta():
    print("\n Tipos de boleta:")
    print(" " + "-"*30)

    for clave, (nombre, factor) in TIPOS_BOLETA.items():
        if factor < 1:
            info = f"({int((1 - factor) * 100)}% descuento)"
        elif factor > 1:
            info = f"({int((factor - 1) * 100)}% recargo)"
        else:
            info = "(precio normal)"

        print(f" [{clave}] {nombre:<15} {info}")

    print(" " + "-"*30)


def seleccionar_pelicula():
    mostrar_cartelera()
    while True:
        try:
            opcion = int(input("\n Ingresa el ID de la película: "))
            if opcion not in PELICULAS:
                raise ValueError("El ID ingresado no corresponde a ninguna película.")
            return opcion, PELICULAS[opcion]
        except ValueError as e:
            print(f" Error: {e} Intenta de nuevo.")


def seleccionar_tipo_boleta():
    mostrar_tipos_boleta()
    while True:
        try:
            opcion = input("\n Elige el tipo de boleta: ").strip()
            if opcion not in TIPOS_BOLETA:
                raise KeyError("Opción inválida. Elige un número del menú.")
            return TIPOS_BOLETA[opcion]
        except KeyError as e:
            print(f" Error: {e} Intenta de nuevo.")


def seleccionar_cantidad():
    while True:
        try:
            cantidad = int(input(" Cantidad de boletas (máx. 10): "))
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a 0.")
            if cantidad > 10:
                raise ValueError("No se pueden comprar más de 10 boletas a la vez.")
            return cantidad
        except ValueError as e:
            print(f" Error: {e} Intenta de nuevo.")


def calcular_total(precio_base, factor, cantidad):
    precio_por_boleta = precio_base * factor
    total = precio_por_boleta * cantidad
    return precio_por_boleta, total


def confirmar_compra(pelicula, tipo_nombre, cantidad, precio_unitario, total):
    print("\n" + "="*45)
    print(" RESUMEN DE COMPRA")
    print("="*45)
    print(f" Película : {pelicula['titulo']}")
    print(f" Género : {pelicula['genero']}")
    print(f" Duración : {pelicula['duracion']} min")
    print(f" Tipo boleta : {tipo_nombre}")
    print(f" Cantidad : {cantidad}")
    print(f" Precio c/u : ${precio_unitario:,.0f}")
    print(f" TOTAL : ${total:,.0f}")
    print("="*45)

    while True:
        confirmacion = input(" ¿Confirmar compra? (s/n): ").strip().lower()
        if confirmacion == "s":
            return True
        elif confirmacion == "n":
            return False
        else:
            print(" Por favor ingresa 's' o 'n'.")


def registrar_compra(id_pelicula, pelicula, tipo_nombre, cantidad, total):
    compra = {
        "id_pelicula": id_pelicula,
        "titulo": pelicula["titulo"],
        "tipo": tipo_nombre,
        "cantidad": cantidad,
        "total": total,
    }
    historial_compras.append(compra)


def mostrar_historial():
    if not historial_compras:
        print("\n No hay compras registradas en esta sesión.")
        return

    print("\n" + "="*55)
    print(" HISTORIAL DE COMPRAS")
    print("="*55)

    gran_total = 0
    for i, compra in enumerate(historial_compras, start=1):
        print(f" #{i} {compra['titulo']} | {compra['tipo']} | {compra['cantidad']} boleta(s) | ${compra['total']:,.0f}")
        gran_total += compra["total"]

    print("-"*55)
    print(f" GRAN TOTAL DE LA SESIÓN: ${gran_total:,.0f}")
    print("="*55)


def procesar_compra():
    print("\n --- NUEVA COMPRA ---")
    id_pelicula, pelicula = seleccionar_pelicula()
    tipo_nombre, factor = seleccionar_tipo_boleta()
    cantidad = seleccionar_cantidad()

    precio_unit, total = calcular_total(pelicula["precio"], factor, cantidad)

    if confirmar_compra(pelicula, tipo_nombre, cantidad, precio_unit, total):
        registrar_compra(id_pelicula, pelicula, tipo_nombre, cantidad, total)
        print("\n ¡Compra realizada con éxito!")
    else:
        print("\n Compra cancelada.")


def menu_principal():
    print("\n" + "*"*45)
    print("* BIENVENIDO AL SISTEMA DE BOLETAS CINE *")
    print("*"*45)

    opciones_menu = (
        ("1", "Comprar boletas"),
        ("2", "Ver historial de compras"),
        ("3", "Ver cartelera"),
        ("4", "Salir"),
    )

    while True:
        print("\n MENÚ PRINCIPAL")
        print(" " + "-"*25)

        for clave, descripcion in opciones_menu:
            print(f" [{clave}] {descripcion}")

        print(" " + "-"*25)

        try:
            opcion = input(" Elige una opción: ").strip()

            if opcion == "1":
                procesar_compra()
            elif opcion == "2":
                mostrar_historial()
            elif opcion == "3":
                mostrar_cartelera()
            elif opcion == "4":
                mostrar_historial()
                print("\n ¡Hasta pronto!\n")
                break
            else:
                raise ValueError("Opción no válida. Elige entre 1 y 4.")

        except ValueError as e:
            print(f" {e}")


# ==================== PUNTO DE ENTRADA ====================
if __name__ == "__main__":
    menu_principal()