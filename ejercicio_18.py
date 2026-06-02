inventario = {
    "manzana": {"precio": 500, "stock": 50},
    "banana":  {"precio": 300, "stock": 30},
    "pera":    {"precio": 700, "stock": 20},
}

def agregar_producto(inv, nombre, precio, stock):
    inv[nombre] = {"precio": precio, "stock": stock}

def actualizar_stock(inv, nombre, cantidad):
    if inv[nombre]["stock"] + cantidad < 0:
        print("Stock insuficiente para " + nombre + ".")
    else:
        inv[nombre]["stock"] += cantidad

def productos_sin_stock(inv):
    lista = []
    for nombre in inv:
        if inv[nombre]["stock"] == 0:
            lista.append(nombre)
    return lista

def valor_total_inventario(inv):
    total = 0
    for nombre in inv:
        total += inv[nombre]["precio"] * inv[nombre]["stock"]
    return total

def mostrar_inventario(inv):
    print("\n=== INVENTARIO ===")
    for nombre in sorted(inv):
        print(nombre + ": $" + str(inv[nombre]["precio"]) + " | Stock: " + str(inv[nombre]["stock"]))

agregar_producto(inventario, "uva", 900, 15)
actualizar_stock(inventario, "banana", -35)
actualizar_stock(inventario, "pera", -20)

mostrar_inventario(inventario)
print("\nSin stock: " + str(productos_sin_stock(inventario)))
print("Valor total: $" + str(valor_total_inventario(inventario)))