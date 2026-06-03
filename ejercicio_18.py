def agregar_producto(inv, nombre, precio, stock):
    inv[nombre] = {"precio": precio, "stock": stock}

def actualizar_stock(inv, nombre, cantidad):
    if nombre in inv:
        nuevo_stock = inv[nombre]["stock"] + cantidad
        if nuevo_stock < 0:
            print(f"Stock insuficiente para {nombre}.\n")
        else:
            inv[nombre]["stock"] = nuevo_stock

def productos_sin_stock(inv):
    return [prod for prod, info in inv.items() if info["stock"] == 0]

def valor_total_inventario(inv):
    total = 0
    for info in inv.values():
        total += info["precio"] * info["stock"]
    return total


def mostrar_inventario(inv):
    print("=== INVENTARIO ===")
    for prod in sorted(inv.keys()):
        print(f"{prod}: ${inv[prod]['precio']} | Stock: {inv[prod]['stock']}")
    print()


inventario = {
    "manzana": {"precio": 500,  "stock": 50},
    "banana":  {"precio": 300,  "stock": 30},
    "pera":    {"precio": 700,  "stock": 20},
}

agregar_producto(inventario, "uva", 900, 15)
actualizar_stock(inventario, "banana", -35)
actualizar_stock(inventario, "pera", -20)
mostrar_inventario(inventario)
print(f"Sin stock: {productos_sin_stock(inventario)}")
print(f"Valor total: ${valor_total_inventario(inventario)}")
