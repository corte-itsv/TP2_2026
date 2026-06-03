def agregar_producto(inv, nombre, precio, stock):
    inv[nombre] = {"precio": precio, "stock": stock}

def actualizar_stock(inv, nombre, cantidad):
    if nombre not in inv:
        print("Producto no encontrado")
        return

    nuevo_stock = inv[nombre]["stock"] + cantidad

    if nuevo_stock < 0:
        print("Stock insuficiente para banana")
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
    print("INVENTARIO")
    print("-" * 35)

    for nombre in sorted(inv):
        datos = inv[nombre]
        print(
            f"{nombre:<10} "
            f"Precio: ${datos['precio']:<5} "
            f"Stock: {datos['stock']}"
        )


# Inventario inicial
inventario = {
    "manzana:": {"precio": 500, "stock": 50},
    "banana:":  {"precio": 300, "stock": 30},
    "pera:":    {"precio": 700, "stock": 20},
}

# Operaciones
agregar_producto(inventario, "uva:", 900, 15)

actualizar_stock(inventario, "banana:", -35)   # Stock insuficiente para banana
actualizar_stock(inventario, "pera:", -20)     # Queda en 0

# Estado final
mostrar_inventario(inventario)

print("\nProductos sin stock:", productos_sin_stock(inventario))
print("Valor total del inventario: $", valor_total_inventario(inventario))