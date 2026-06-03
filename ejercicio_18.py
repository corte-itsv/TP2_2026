def agregar_producto(inv, nombre, precio, stock):
    inv[nombre] = {"precio": precio, "stock": stock}

def actualizar_stock(inv, nombre, cantidad):
    if nombre not in inv:
        return

    nuevo_stock = inv[nombre]["stock"] + cantidad
    if nuevo_stock < 0:
        print(f"Stock insuficiente para {nombre}.")
        return

    inv[nombre]["stock"] = nuevo_stock

def productos_sin_stock(inv):
    sin_stock = []
    for nombre, datos in inv.items():
        if datos["stock"] == 0:
            sin_stock.append(nombre)
    return sin_stock

def valor_total_inventario(inv):
    total = 0
    for datos in inv.values():
        total += datos["precio"] * datos["stock"]
    return total

def mostrar_inventario(inv):
    print("=== INVENTARIO ===")
    for nombre in sorted(inv):
        datos = inv[nombre]
        print(f"{nombre}: ${datos['precio']} | Stock: {datos['stock']}")

inventario = {
    "manzana": {"precio": 500, "stock": 50},
    "banana": {"precio": 300, "stock": 30},
    "pera": {"precio": 700, "stock": 20},
}

agregar_producto(inventario, "uva", 900, 15)
actualizar_stock(inventario, "banana", -35)
actualizar_stock(inventario, "pera", -20)

print()
mostrar_inventario(inventario)

sin_stock = productos_sin_stock(inventario)
valor_total = valor_total_inventario(inventario)

print()
print(f"Sin stock: {sin_stock}")
print(f"Valor total: ${valor_total}")