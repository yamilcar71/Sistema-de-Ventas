from cliente import Cliente
from producto import Producto
from venta_detalle import VentaDetalle
from venta import Venta
""" crear un CRUD de cliente"""
datos_inicial:list=[{"dni":"71706587",
                     "nombres":"Yuber luis ",
                     "apellidos":"luna gutierrez",
                     "direccion":"salida arequipa " ,
                     "telefono":"900345610"},

                     {"dni":"73820194",
                     "nombres":"wilder",
                     "apellidos":"Arenas  Arenas ",
                     "direccion":"salida arequipa " ,
                     "telefono":"966424725"},

                     {"dni":"71652863",
                     "nombres":"jamil neftali",
                     "apellidos":"ccari cari",
                     "direccion":"Jr azangaro" ,
                     "telefono":"967027952"}
                     ]
lista_clientes:Cliente=[]


def cargar_cliente():
    for dato in datos_inicial:
    
        lista_clientes.append(Cliente(dato["dni"],
                                      dato["nombres"],
                                      dato["apellidos"],
                                      dato["direccion"],
                                      dato["telefono"]))
    return listar_cliente
def insertar_cliente():
    dni:str = input("Ingrese el DNI del cliente: ")
    nombres:str = input("ingrese el nombre del cliente: ")
    apellidos:str = input("ingrese apellidos del cliente: ")
    direccion:str = input("ingrese la direccion del cliente: ")
    telefono:str = input("ingrese el telefono del cliente : ")
    lista_clientes.append(Cliente(len(listar_cliente)+1,dni,nombres,apellidos,direccion,telefono))
    return lista_clientes

def listar_cliente():
    print("======================LISTA DE PERSONAS=========================")
    print("================================================================")
    print("|ID|  DNI   |   NOMBRES  |  APELLIDOS  |  DIRECCION | TELEFONO|")
    print("================================================================")
    for clien in lista_clientes:
        print("_______________________________________________________________")
        print(clien.convertir_a_string())
        print("_______________________________________________________________")

def bucar_cliente():
    dni:str = input("Ingrese el DNI del cliente: ")
    for cliente in lista_clientes:
        if cliente.dni == dni:
            print(cliente.convertir_a_texto())
            return cliente

def editar_cliente():
    listar_cliente()
    dni:str = input("ingrese el Dni del cliente: ")
    for cliente in lista_clientes:
        if cliente.dni == dni:
            print(cliente.convertir_a_string())
            cliente.dni = input("Ingrese DNI del cliente: ")
            cliente.nombres = input("Ingrese nombre del cliente: ")
            cliente.apellidos = input("ingrese  apellidos del cliente: ")
            cliente.direccion = input("ingrese direccion del cliente: ")
            cliente.telefono = input("ingrese el telefono del cliente: ")
    listar_cliente()

def eliminar_cliente():
    listar_cliente()
    dni:str = input("ingrese el dni del cliente: ")
    for index, cliente in enumerate(lista_clientes):
        if cliente.dni == dni:
            lista_clientes.pop(index)
    listar_cliente()



""" crear un CRUD de producto"""
datos_inicial_productos:list=[{"codigo":"001",
                            "nombre":"Toyota for",
                            "precio":2.50,
                            "placa":"xzx320",
                            "color":"negro",
                            "motor":"1300"},
                           {"codigo":"002",
                            "nombre":"BMW",
                            "precio":2.00,
                            "placa":"zrs203",
                            "color":"azul",
                            "motor":"2000"},
                           {"codigo":"003",
                           "nombre":"ferrari",
                           "precio":8.00,
                           "placa": "z4145d",
                           "color":"morado",
                           "motor":"2500"}]
                     
                      
lista_productos:Producto=[]


def cargar_productos():
    for dato in datos_inicial_productos:
        lista_productos.append(Producto(
                                dato["codigo"],
                                dato["nombre"],
                                dato["precio"],
                                dato["placa"],
                                dato["color"],
                                dato["motor"],))
    return lista_productos
def insertar_producto():
    codigo:str = input("Ingrese el codigo del producto: ")
    nombre:str = input("ingrese el nombre del producto: ")
    precio:float = float(input("ingrese precio del producto: "))
    placa:str = input("Ingrse la placa del producto")
    color:str = input("Ingrse el color del producto")
    motor:str = input("Ingrse el motor del producto")
    
    lista_productos.append(Producto(codigo,nombre,precio,placa,color,motor,))
    return lista_productos

def listar_productos():
    print("======================LISTA DE PRODUCTOS=========================")
    print("================================================================")
    print("|CODIGO|  NOMBRE   |   PRECIO  | PLACA | COLOR | MOTOR |")
    print("================================================================")
    for producto in lista_productos:
        print("_______________________________________________________________")
        print(producto.convertir_a_string())
        print("_______________________________________________________________")

def bucar_producto():
    codigo:str = input("Ingrese el codigo del producto: ")
    for producto in lista_productos:
        if producto.codigo == codigo:
            print(producto.convertir_a_texto())
            return producto

def editar_producto():
    listar_productos()
    codigo:str = input("ingrese codigo del producto: ")
    for producto in lista_productos:
        if producto.codigo == codigo:
            print(producto.convertir_a_string())
            producto.nombre = input("Ingrese nombre del producto: ")
            producto.precio = input("ingrese  precio del producto: ")
            producto.placa = input("Ingrse la plca del producto")
            producto.color = input("Igrese el color del producto")
            producto.motor = input("Ingrese el motor del producto")
            
    listar_productos()

def eliminar_producto():
    listar_productos()
    codigo:str = input("ingrese codigo del producto: ")
    for index, producto in enumerate(lista_productos):
        if producto.codigo == codigo:
            lista_productos.pop(index)
    listar_productos()
    return lista_productos
venta_detalles:VentaDetalle=[]

def agregar_productos():
    producto:Producto=bucar_producto()
    cantidad:float=float(input("Ingrese la cantidad: "))
    venta_detalles.append(VentaDetalle(len(venta_detalles)+1,producto.codigo,producto.nombre,cantidad,producto.precio,))
    return venta_detalles
ventas:Venta=[]
def insertar_venta():
    cliente:Cliente=bucar_cliente()
    continuar_agregando_producto:bool=True
    while continuar_agregando_producto:
        opcion:str=input("1 para agregar producto, 2 para guardar venta: ")
        match opcion:
            case "1":
                agregar_productos()
            case "2":
                continuar_agregando_producto=False
    total_venta:float=0
    for venta_detalle in venta_detalles:
        print(venta_detalle.convertir_a_texto())
        total_venta=total_venta+venta_detalle.total
    venta:Venta=Venta(len(ventas)+1,cliente,venta_detalles,total_venta)
    ventas.append(venta)
    return ventas
def listar_ventas():
    for venta in ventas:
        print(venta.convertir_a_texto())
    return ventas

def buscar_venta():
    numero:int=int(input("Ingrese el numero de la venta: "))
    for venta in ventas:
        if venta.numero==numero:
            for detalle in venta.detalle:
                print(detalle.convertir_a_texto())
            return venta


def menu_texto():
    print("=============MENU============")
    print("=========CRUD PERSONA========")
    print("OPCION 1 PARA CREAR PERSONA")
    print("OPCION 2 PARA LISTAR")
    print("OPCION 3 PARA BUSCAR PERSONA")
    print("OPCION 4 PARA EDITAR PERSONA")
    print("OPCION 5 PARA ELIMINAR PERSONA")
    print("=========CRUD PRODUCTO========")
    print("OPCION 6 PARA CREAR PRODUCTO")
    print("OPCION 7 PARA LISTAR PRODUCTO")
    print("OPCION 8 PARA BUSCAR PRODUCTO")
    print("OPCION 9 PARA EDITAR PRODUCTO")
    print("OPCION 10 PARA ELIMINAR PRODUCTO")
    print("=========CRUD VENTA========")
    print("OPCION 11 PARA REGISTRAR VENTA")
    print("OPCION 12 PARA LISTAR VENTA")
    print("OPCION 13 PARA BUSCAR VENTA")
    print("OPCION 30 PARA SALIR")

def menu():
    continuar:bool=True
    while continuar:
        menu_texto()  
        opcion:str
        opcion = input("Ingrese la opcion: ")
        match opcion:
            case "1":
                insertar_cliente()
            case "2": 
                listar_cliente()
            case "3":
                bucar_cliente()
            case "4":
                editar_cliente()
            case "5":
                eliminar_cliente()
            case "6":
                insertar_producto()
            case "7": 
                listar_productos()
            case "8":
                bucar_producto()
            case "9":
                editar_producto()
            case "10":
                eliminar_producto()
            case "11":
                insertar_venta()
            case "12":
                listar_ventas()
            case "13":
                buscar_venta()
            case "30":
                print("Saliendo del programa")
                continuar = False

def main():
    cargar_cliente()
    cargar_productos()
    menu()    
    print("Iniciando programa")
    return True

if __name__== '__main__':
    main()