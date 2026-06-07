inventario = {
    "manzana": {"precio": 500, "stock": 50},
    "banana":  {"precio": 300, "stock": 30},
    "pera":    {"precio": 700, "stock": 20},
}

def agregar_producto(inv, nombre, precio, stock):
    inv[nombre] = {"precio": precio, "stock": stock}

def actualizar_stock(inv, nombre, cantidad):
    nuevo_stock = inv[nombre]["stock"] + cantidad
    if nuevo_stock < 0:
        print(f"Stock insuficiente para {nombre}.")
    else:
        inv[nombre]["stock"] = nuevo_stock

def productos_sin_stock(inv):
    return [nombre for nombre, datos in inv.items() if datos["stock"] == 0]

def valor_total_inventario(inv):
    return sum(datos["precio"] * datos["stock"] for datos in inv.values())

def mostrar_inventario(inv):
    print("=== INVENTARIO ===")
    for nombre in sorted(inv):
        datos = inv[nombre]
        print(f"{nombre}: ${datos['precio']} | Stock: {datos['stock']}")

# Operaciones
agregar_producto(inventario, "uva", 900, 15)
actualizar_stock(inventario, "banana", -35)   # Stock insuficiente
actualizar_stock(inventario, "pera", -20)     # Queda en 0

# Estado final
mostrar_inventario(inventario)
print(f"\nSin stock: {productos_sin_stock(inventario)}")
print(f"Valor total: ${valor_total_inventario(inventario)}")