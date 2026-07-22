inventario = {
    "manzana": {"precio": 500,  "stock": 50},
    "banana":  {"precio": 300,  "stock": 30},
    "pera":    {"precio": 700,  "stock": 20},
}


def agregar_producto(inv, nombre, precio, stock):
    inv[nombre] = {"precio" : precio, "stock" : stock}
    
def actualizar_stock(inv, nombre, cantidad):
    stock_actual = inv[nombre]["stock"]
    stock_actualizado = stock_actual + cantidad
    if stock_actualizado < 0:
        print("Stock insuficiente para", nombre)
    else:
        inv[nombre]["stock"] = stock_actualizado

def productos_sin_stock(inv):
    lista_de_productos_sin_stock = []
    for nombre, info in inv.items():
        if info["stock"] == 0:
            lista_de_productos_sin_stock.append(nombre)
    return lista_de_productos_sin_stock            

def valor_total_inventario(inv):
    precio_total = 0
    for nombre, info in inv.items():
        calculo = info["precio"] * info["stock"]
        precio_total = precio_total + calculo
    return precio_total

def mostrar_inventario(inv):
    for nombre, info in inv.items():
        print(f"{nombre}: ${info["precio"]} | Stock: {info["stock"]}")


agregar_producto(inventario, "uva", 900, 15)

actualizar_stock(inventario, "banana", -35)
print("")
actualizar_stock(inventario, "pera", -20)

print("======== INVENTARIO ========")

mostrar_inventario(inventario)

print("")

lista_de_productos_sin_stock = productos_sin_stock(inventario)
print("Sin stock:", lista_de_productos_sin_stock)

precio_total = valor_total_inventario(inventario)
print(precio_total)