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
    
#4. Genera una función que calcule la diferencia entre los valores de dos listas.
#Usa la función map()

def diferencia_listas(lista1, lista2):

    """Calcula la diferencia elemento a elemento entre dos listas de números.

    Args:
        lista1 (list): Primera lista de números.
        lista2 (list): Segunda lista de números.

    Returns:
        list: Lista con la diferencia (lista1[i] - lista2[i]) de cada par.
    """

    return list(map(lambda x, y: x - y, lista1, lista2))

lista1 = [10, 20, 30]
lista2 = [1, 2, 3]
print(diferencia_listas(lista1, lista2))

#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
#defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
#que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
#una tupla que contenga la media y el estado.

def evaluar_notas(numeros, nota_aprobado=5):
    
    """Calcula la media de una lista de números y determina si aprueba.

    Args:
        numeros (list | tuple): Lista o tupla de números a evaluar.
        nota_aprobado (int, optional): Nota mínima para aprobar. Defaults to 5.

    Returns:
        tuple: Una tupla con la media (float) y el estado ("aprobado" o "suspenso").
    """

    
    media = sum(numeros) / len(numeros)
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    return media, estado


numeros = (4, 3, 5, 8, 9)
print(evaluar_notas(numeros))

#6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    """Calcula el factorial de un número de manera recursiva.

    Args:
        n (int): Número para calcular el factorial.

    Returns:
        int: Factorial del número.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = 3
print(factorial(numero))








    