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

#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    """Convierte una lista de tuplas a una lista de strings.

    Args:
        lista_tuplas (list): Lista de tuplas.

    Returns:
        list: Lista de strings.
    """
    return list(map(str, lista_tuplas))

nota = [(1, 2), (3, 4), (5, 6)]
print(tuplas_a_strings(nota))

#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
#o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
#indicando si la división fue exitosa o no.

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número:"))
    resultado = num1 / num2
    print(f"División exitosa: {resultado}")
except ValueError:
    print("Error: Debe ingresar un valor numérico.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
#"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def excluir_mascotas(mascotas):
    '''Excluye ciertas mascotas prohibidas en España de una lista de nombres de mascotas.
    
    Args:
        mascotas (list): Lista de nombres de mascotas.
    Returns:
        list: Nueva lista de mascotas excluyendo las prohibidas.
               
    '''
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, mascotas)) 

animales = ["Perro", "Gato", "Mapache", "Tigre", "Conejo", "Cocodrilo", "Oso"]
print(excluir_mascotas(animales))

#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
#excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    """Excepción personalizada para indicar que la lista está vacía."""
    pass
def calcular_promedio(numeros):
    '''Calcula el promedio de una lista de números.

    Args:
        numeros (list): lista de números.
    Returns:
        float: Promedio de los números en la lista.
    '''
    if not numeros:
        raise ListaVaciaError("La lista está vacía. No se puede calcular el promedio.")
    return sum(numeros) / len(numeros)
print("-----Prueba con la lista vacía-----")
try:
    print(calcular_promedio([]))
except ListaVaciaError as error:
    print(f"Error: {error}")

print("---Prueba con lista con datos---")
promedio = calcular_promedio([10, 20, 30, 40, 50])
print(f"El promedio es: {promedio}")

#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
#valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
#adecuadamente.

class EdadInvalidaError(Exception):
    """Excepción personalizada para indicar que la edad ingresada es inválida."""
    pass
try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0 or edad > 120:
        raise EdadInvalidaError("La edad debe estar entre 0 y 120.")
    print(f"Tu edad es: {edad}")
except ValueError:
    print("Error: debes introducir un número entero")
except EdadInvalidaError as error:
    print(f"Error: {error}")

#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitudes_palabras(frase):
    """Devuelve una lista con la longitud de cada palabra en una frase.
    Args:
        frase (str): la frase a analizar.
    Returns:
        list: una lista con la longitud de cada palabra.
    """
    palabras = frase.split()
    return list(map(len, palabras))

frase = "Hola mundo, esto es una prueba"
print(longitudes_palabras(frase))

#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
#mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def mayus_minus(conjunto_letras):
    """Devuelve una lista de tuplas con cada letra en mayúsculas y minúsculas, sin repeticiones.
    Args:
        conjunto_letras (set): un conjunto de caracteres.
        
    Returns:
        list: una lista de tuplas con cada letra en mayúsculas y minúsculas.
    """
    
    
    return list(map(lambda letra: (letra.upper(), letra.lower()), conjunto_letras))

conjunto = {'a', 'b', 'c'}
print(mayus_minus(conjunto))

#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
#función filter()

def palabras_que_empiezan(lista_palabra, letra):
    """Devuelve una lista de palabra y que comience con una letra específica.
    Args:
        lista_palabra (list): Lista de palabras a filtrar.
        letra (str): Letra por la que debe empezar la palabra.
            
    Returns:
        list: Lista de palabras que comience con una letra especifica.

    
    """
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabra))

fruta = palabras_que_empiezan(["manzana", "pera", "naranja", "fresa", "platano"], "n")
print(fruta)

#15. Crea una función lambda que sume 3 a cada número de una lista dada.

sumar_tres = lambda x: x + 3
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = list(map(sumar_tres, numeros))
print(resultado)

     
    
    
    





