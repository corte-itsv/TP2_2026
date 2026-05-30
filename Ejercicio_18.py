def agregar_producto(inv, nombre, precio, stock):
    inv[nombre] = {"precio": precio, "stock": stock}

def actualizar_stock(inv, nombre, cantidad):
    if inv[nombre]["stock"] + cantidad < 0:
        print(f"Stock insuficiente para {nombre}.")
    else:
        inv[nombre]["stock"] += cantidad

def productos_sin_stock(inv):
    return [nombre for nombre, datos in inv.items() if datos["stock"] == 0]

def valor_total_inventario(inv):
    return sum(datos["precio"] * datos["stock"] for datos in inv.values())

def mostrar_inventario(inv):
    print("=== INVENTARIO ===")
    for nombre, datos in sorted(inv.items()):
        print(f"{nombre}: ${datos['precio']} | Stock: {datos['stock']}")


inventario = {
    "manzana": {"precio": 500, "stock": 50},
    "banana":  {"precio": 300, "stock": 30},
    "pera":    {"precio": 700, "stock": 20},
}

agregar_producto(inventario, "uva", 900, 15)
actualizar_stock(inventario, "banana", -35)
actualizar_stock(inventario, "pera", -20)

mostrar_inventario(inventario)
print(f"\nSin stock: {productos_sin_stock(inventario)}")
print(f"Valor total: ${valor_total_inventario(inventario)}")