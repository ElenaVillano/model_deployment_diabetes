def obtener_nombre_completo(nombre, apellido):
    nombre_completo = nombre.title() + " " + apellido.title()
    return nombre_completo

print(obtener_nombre_completo("Elena", "Villalobos"))

def sumar(n1:int, n2:int) -> float:
    return n1 + n2

print(sumar(2.5, 2.5))

from typing import List

def procesar_items(items: List[str]):
    for item in items:
        print(item)

procesar_items(['1','2','3','4'])


from typing import List,Set,Tuple,Dict,Optional

def procesar_items_dict(prices:Dict[str,float]):
    for price_name,value in prices.items():
        print(price_name + " " + str(value))

procesar_items_dict({'dolar':25.00})


def decir_hola(nombre: Optional[str]=None):
    if nombre is not None:
        print(f'Hola {nombre}')
    else:
        print('Hola Mundo')

decir_hola('elena')
decir_hola()