import json
import datetime

lista_transacciones = []
id_vehiculo = 2
id_cliente = 1 
tipo_tran = 'Compra'

# Primero leo y serializo el JSON
try:
  with open('transacciones.json', 'r', encoding='utf-8') as actual_json:
    lista_transacciones = json.load(actual_json)
except FileNotFoundError:
  lista_transacciones = []


# GENERO EL NUEVO ID
def buscar_nuevo_id(lista):
  id = 0
  if(len(lista)== 0):
    return id
  else:
    ultimo_elemento = lista[-1]
    ultimo_elemento_id = ultimo_elemento['id_transaccion']
    id = ultimo_elemento_id + 1
    return id
  

# FUNCION QUE GENERA UNA FECHA
def generar_fecha():
  fecha = datetime.datetime.now()
  fecha_str = fecha.strftime('%Y-%m-%d')
  return fecha_str


# BUSCO EL VALOR DEL VEHICULO
def buscar_monto(id_vehiculo, tipo_transaccion):
  tipo_transaccion = tipo_transaccion.lower()
  with open('vehiculos.json', 'r', encoding='utf-8') as r_json:
    lista_vehiculos = json.load(r_json)
    for vehiculo in lista_vehiculos:
      if(vehiculo['id_vehiculo'] == id_vehiculo and tipo_transaccion == 'venta'):
        return vehiculo['precio_venta']
      elif (vehiculo['id_vehiculo'] == id_vehiculo and tipo_transaccion == 'compra'):
        return vehiculo['precio_compra']


# GENERO UNA OBSERVACION
def generar_observacion(tipo_tran):
  tipo_tran = tipo_tran.lower()
  if(tipo_tran == 'venta'):
    return 'Venta realizada con exito'
  else:
    return 'Compra realizada con exito'


# GENERO LA NUEVA TRANSACCION
def generar_nueva_transaccion(id_vehiculo, id_cliente, tipo_tran ):
  nueva_transaccion = {}
  nueva_transaccion['id_transaccion'] = buscar_nuevo_id(lista_transacciones)
  nueva_transaccion['id_vehiculo'] = id_vehiculo
  nueva_transaccion['id_cliente'] = id_cliente
  nueva_transaccion['tipo_transaccion'] = tipo_tran
  nueva_transaccion['fecha'] = generar_fecha()
  nueva_transaccion['monto'] = buscar_monto(id_vehiculo, tipo_tran)
  nueva_transaccion['observaciones'] = generar_observacion(tipo_tran)
  return nueva_transaccion
  
def agregar_transaccion_json(lista_transacciones):
  with open('transacciones.json', 'w', encoding='utf-8') as json_file:
    lista_transacciones.append(generar_nueva_transaccion(id_vehiculo, id_cliente, tipo_tran))
    json.dump(lista_transacciones, json_file, ensure_ascii=False, indent=4)
    
  
agregar_transaccion_json(lista_transacciones)
  