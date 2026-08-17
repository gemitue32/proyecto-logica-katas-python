#1. Escribe una función que reciba una cadena de texto como parámetro 
# y devuelva un diccionario con las frecuencias
#de cada letra en la cadena. Los espacios no deben ser considerados.

def contar_frecuencias(cadena):
    """ Cuenta la frecuencia de cada letra en una cadena de texto, 
    ignorando los espacios.
    Args:
        cadena (str): La cadena de texto a analizar.
    Returns:
        dict: Un diccionario con las frecuencias de cada letra.
    """
    frecuencias = {}
    for letra in cadena:
        if letra != ' ':
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

frecuencia = contar_frecuencias("Hola mundo")
print(frecuencia)

#2. Dada una lista de números
# obtén una nueva lista con el doble de cada valor. Usa la función map()

def obtener_dobles(numeros):

    """ Obtiene una nueva lista con el doble de cada valor en la lista original.
    Args:
        numeros (list): Una lista de números.
    Returns:
        list: Una nueva lista con el doble de cada valor.
    """
    return list(map(lambda x: x * 2, numeros))


numeros = [10, 20, 30, 40, 50]
dobles = obtener_dobles(numeros)
print(dobles)

#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
#La función debe devolver una lista con todas las palabras de la lista original
#que contengan la palabra objetivo.

def filtrar_palabras(palabras, objetivo):
    """ Filtra las palabras que contienen la palabra objetivo.
    Args:
        palabras (list): Una lista de palabras.
        objetivo (str): La palabra objetivo a buscar.
    Returns:
        list: Una lista con las palabras que contienen la palabra objetivo.
    """
    resultado = []
    for palabra in palabras:
        if objetivo in palabra:
            resultado.append(palabra)
    return resultado


compra = ["manzana", "banana", "naranja", "pera", "sandía"]
resultado = filtrar_palabras(compra, "ana")
print(resultado)







    