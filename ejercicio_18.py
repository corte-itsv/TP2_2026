def agregar_producto(inv, nombre, precio, stock):
    if nombre in inv:
        return "El producto ya existe"
    else:
        inv[nombre] = {"precio": precio, "stock": stock}
        return "Producto agregado"


def actualizar_stock(inventario, producto, cantidad):
    if producto not in inventario: 
        return "Producto no encontrado" 
    elif inventario[producto]["stock"] < cantidad:
        return f"Stock insuficiente para {producto}"
    inventario[producto]["stock"] -= cantidad 
    return "Stock actualizado"


def productos_sin_stock(inv):
    sin_stock = []
    for nombre, info in inv.items():
        if info["stock"] == 0:
            sin_stock.append(nombre)
    return sin_stock  # Move return outside the loop


def valor_total_inventario(inv):
    total = 0
    for info in inv.values():
        total += info["precio"] * info["stock"]
    return total


def mostrar_inventario(inventario): 
    if not inventario: 
        return "Inventario vacío" 
    lineas = [f"{producto}: {cantidad}" for producto, cantidad in sorted(inventario.items(), key=lambda it: it[0].lower())]
    return "\n".join(lineas)


inventario = {
    "manzana": {"precio": 500,  "stock": 50},
    "banana":  {"precio": 300,  "stock": 30},
    "pera":    {"precio": 700,  "stock": 20},
}

print(inventario)
print(agregar_producto(inventario, "uva", 900, 15))
print(actualizar_stock(inventario, "banana", -35))  
print(actualizar_stock(inventario, "pera", -20))    
print(mostrar_inventario(inventario))
