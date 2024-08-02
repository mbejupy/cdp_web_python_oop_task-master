from customer import Customer
from item import Item
from seller import Seller

# Crear un vendedor con nombre "DIC Almacenar"
seller = Seller("DIC Almacenar")
for i in range(10):
    Item("SSD de 2.5 pulgadas", 13370, seller)
    Item("HDD de 3.5 pulgadas", 10980, seller)
    Item("CPU", 40830, seller)
    Item("Refrigerador de CPU", 13400, seller)
    Item("SSD M.2", 12980, seller)
    Item("Caja de PC", 8727, seller)
    Item("Tarjeta gráfica", 23800, seller)
    Item("Placa madre", 28980, seller)
    Item("Memoria", 13880, seller)
    Item("Fuente de alimentación", 8980, seller)

# Solicitar al usuario que introduzca su nombre y crear un cliente con ese nombre
print("🤖 Por favor, introduce tu nombre")
customer = Customer(input())

# Solicitar al usuario que introduzca la cantidad de dinero a recargar en su billetera y depositarlo
print("🏧 Por favor, introduce la cantidad a recargar en tu billetera")
customer.wallet.deposit(int(input()))

# Iniciar el proceso de compras
print("🛍️ Comenzando compras")
end_shopping = False

# Bucle principal para realizar las compras
while not end_shopping:
    # Mostrar la lista de productos disponibles por el vendedor
    print("📜 Lista de productos")
    seller.show_items()

    # Solicitar al usuario que seleccione un producto por su número
    print("️️⛏ Por favor, introduce el número del producto")
    number = int(input())

    # Solicitar al usuario que introduzca la cantidad deseada del producto
    print("⛏ Por favor, introduce la cantidad del producto")
    quantity = int(input())

    # Obtener los productos seleccionados del vendedor y agregarlos al carrito del cliente
    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)

    # Mostrar los productos actuales en el carrito del cliente y el monto total
    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 Monto total: {customer.cart.total_amount()}")

    # Verificar si el saldo de la billetera del cliente es suficiente para continuar comprando
    if customer.wallet.balance < customer.cart.total_amount():
        print("No tienes suficiente saldo en la billetera para comprar más productos.")
        print("¿Deseas recargar tu billetera? (si/no)")

        # Preguntar al usuario si desea recargar su billetera si no tiene suficiente saldo
        if input().lower() == "si":
            print("🏧 Por favor, introduce la cantidad a recargar en tu billetera")
            customer.wallet.deposit(int(input()))
            continue  # Continuar con el ciclo de compras

        break  # Salir del ciclo de compras si el usuario no desea recargar la billetera

    # Preguntar al usuario si desea finalizar las compras
    print("😭 ¿Deseas finalizar las compras? (si/no)")
    end_shopping = input().lower() == "si"

# Procesar la compra si el usuario decide finalizar las compras
if end_shopping:
    print("💸 ¿Deseas confirmar la compra? (si/no)")

    # Preguntar al usuario si desea confirmar la compra
    if input().lower() == "si":
        customer.cart.check_out()  # Procesar la compra

    # Mostrar resultados finales de la compra y los saldos
    print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultados ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
    print(f"️🛍️ ️Productos de {customer.name}")
    customer.show_items()
    print(f"😱👛 Saldo en la billetera de {customer.name}: {customer.wallet.balance}")

    print(f"📦 Estado del inventario de {seller.name}")
    seller.show_items()
    print(f"😻👛 Saldo en la billetera de {seller.name}: {seller.wallet.balance}")

    # Mostrar el contenido final del carrito y el monto total
    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🌚 Monto total: {customer.cart.total_amount()}")

# Mensaje de finalización
print("🎉 Fin")