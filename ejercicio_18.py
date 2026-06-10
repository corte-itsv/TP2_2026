def agregar_producto(inv, nombre, precio, stock):
    if nombre in inv:
        return "El producto ya existe"
    else:
        inv[nombre] = {"precio": precio, "stock": stock}
        return "Producto agregado"


def actualizar_stock(inv, nombre, cantidad):
    if nombre in inv:
        inv[nombre]["stock"] += cantidad
        return "Stock actualizado"
    else:
        return "Stock insuficiente"


def productos_sin_stock(inv):
    sin_stock = []
    for nombre, info in inv.items():
        if info ["stock"] == 0:
            sin_stock.append(nombre)
        return sin_stock


def valor_total_inventario(inv):
    total = 0
    for info in inv.values():
        total += info["precio"] * info["stock"]
    return total


def mostrar_inventario(inv):
    if len(inv) == 0:
        return "El inventario está vacío"
    else:
        productos = [f"{nombre}: Precio ${info['precio']}, Stock {info['stock']}" for nombre, info in sorted(inv.items())]
        return "\n".join(productos)


inventario = {
    "manzana": {"precio": 500,  "stock": 50},
    "banana":  {"precio": 300,  "stock": 30},
    "pera":    {"precio": 700,  "stock": 20},
}

print(inventario)
print(agregar_producto(inventario, "uva", 900, 15))
print(actualizar_stock(inventario, "banana", -35))
print(actualizar_stock(inventario, "pera", -20) )

