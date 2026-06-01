inventario = {
    "manzana": {"precio": 500, "stock": 50},
    "banana": {"precio": 300, "stock": 30},
    "pera": {"precio": 700, "stock": 20},
}


def agregar_producto(inv, nombre, precio, stock):
    inv[nombre] = {
        "precio": precio,
        "stock": stock
    }


def actualizar_stock(inv, nombre, cantidad):
    if nombre not in inv:
        return

    nuevo_stock = inv[nombre]["stock"] + cantidad

    if nuevo_stock < 0:
        print(f"Stock insuficiente para {nombre}.")
    else:
        inv[nombre]["stock"] = nuevo_stock


def productos_sin_stock(inv):
    return [
        nombre
        for nombre, datos in inv.items()
        if datos["stock"] == 0
    ]


def valor_total_inventario(inv):
    total = 0

    for datos in inv.values():
        total += datos["precio"] * datos["stock"]

    return total


def mostrar_inventario(inv):
    print("\n=== INVENTARIO ===")

    for nombre in sorted(inv):
        print(
            f"{nombre}: "
            f"${inv[nombre]['precio']} | "
            f"Stock: {inv[nombre]['stock']}"
        )


agregar_producto(inventario, "uva", 900, 15)

actualizar_stock(inventario, "banana", -35)
actualizar_stock(inventario, "pera", -20)

mostrar_inventario(inventario)

print("\nSin stock:", productos_sin_stock(inventario))
print("Valor total: $", valor_total_inventario(inventario), sep="")