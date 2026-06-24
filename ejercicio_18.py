def agregar_producto(inv, nombre, precio, stock):
    inv[nombre] = {"precio": precio, "stock": stock}

def actualizar_stock(inv, nombre, cantidad):
        nuevo_stock = inv[nombre]["stock"] + cantidad
        if nuevo_stock >= 0:
            inv[nombre]["stock"] = nuevo_stock
        else:
            print(f"Stock insuficiente de {nombre}.")

def productos_sin_stock(inv):
    lista_de_productos_sin_stock = []
    for nombre in inv:
        if inv[nombre]["stock"] == 0:
            lista_de_productos_sin_stock.append(nombre)
    return lista_de_productos_sin_stock

def valor_total_inventario(inv):
    valor_total = 0
    for nombre in inv:
        valor_total = valor_total + inv[nombre]["precio"] * inv[nombre]["stock"]
    return valor_total



def mostrar_inv(inv):
    for nombre in inv:
        print(nombre, ":", "$", inv[nombre]["precio"], "|", "Stock: ", inv[nombre]["stock"])



inventario = {
    "manzana": {"precio": 500,  "stock": 50},
    "banana":  {"precio": 300,  "stock": 30},
    "pera":    {"precio": 700,  "stock": 20},
}


actualizar_stock(inventario, "banana", - 35)
print("")
print("=== INVENTARIO ===")
agregar_producto(inventario, "uva", 900, 15)
actualizar_stock(inventario, "pera", - 20)
mostrar_inv(inventario)
print("")
lista_sin_stock = productos_sin_stock(inventario)
print("Sin Stock: ", lista_sin_stock)
cantidad_de_plata_total = valor_total_inventario(inventario)
print("Valor total: ", cantidad_de_plata_total)

