"""
--------------------------- COLECCIONES ---------------------------
En este taller aprenderás a manipular coleccciones de datos: Listas, diccionarios, tuplas y sets.
"""

"""
 --- LISTAS ---
Las listas son ordenadas y mutables.
Pueden contener elementos duplicados.
Puedes modificar, añadir y eliminar elementos.
"""
"""
--- Ejercicio 1 Listas ---
Crea una variable "mascotas" que almacene una lista con los siguientes elementos: 'perro', 'gato', 'loro'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
mascotas:["perro","gato","loro"]

print(mascotas)

print(len(mascotas))

print(mascotas[2])

mascotas.append ("tortuga")
print("mascotas")

mascotas[1] = "conejo"
print(mascotas)

mascotas.remove("perro")
print(mascotas)


"""
 --- TUPLAS ---
Las tuplas son ordenadas e inmutables.
Pueden contener elementos duplicados.
No puedes modificar, añadir o eliminar elementos después de la creación.
"""

"""
--- Ejercicio 2 Tuplas ---
Crea una variable "plantas" que almacene una tupla con los siguientes elementos: 'cactus', 'orquidea', 'rosas'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""

plantas:( "cactus","orquidea","rosas")
print(plantas)

print(len(plantas))

print(plantas[2])

plantas[1] = 'hoja rota'

""" Al intentar cambiar un elemento, Python muestra un error."""


"""
 --- SETS ---
Los sets son desordenados y mutables.
No pueden contener elementos duplicados.
Puedes añadir y eliminar elementos, pero no puedes modificar los elementos existentes.
"""

"""
--- Ejercicio 3 Sets ---
Crea una variable "nombres" que almacene un set con los siguientes elementos: 'María', 'Cris', 'Cris', 'Alex'
Imprime por la terminal dicha variable
Haz los pasos pedidos

"""
nombres = {"María", "Cris", "Cris", "Alex"}

print(nombres)

""" El set elimina los elementos repetidos,Por 'Cris' aparece solo una vez."""

print(len(nombres))

""" No se puede acceder a un elemento por posición porque los sets no tienen índices."""

nombres.add("Laura")
print(nombres)

nombres.remove("Alex")
print(nombres)

"""
 --- DICCIONARIOS ---
Los diccionarios son desordenados y mutables.
Contienen pares clave-valor.
Puedes añadir, modificar y eliminar pares clave-valor.
"""

"""
--- Ejercicio 4 Diccionarios ---
Crea un diccionario llamado "ciudad" con las claves 'nombre' y 'pais' y los valores 'Barcelona' y 'España' respectivamente.
Imprime el diccionario 
"""

ciudad = {

    "nombre":"Barcelona"
    "País":"España"

}
print ("ciudad")

print (ciudad["nombre"])


ciudad["continente"] = "Europa"

print(ciudad)

ciudad["nombre"] = "Madrid"

print(ciudad)

del ciudad["continente"]

print(ciudad)