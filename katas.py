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

#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
#todas las palabras que sean más largas que n. Usa la función filter()

def palabras_mas_largas(cadena, n):
    """Devuelve una lista de palabras que sean más largas que n.
    Args:
        cadena (str): Cadena de texto.
        n (int): Número entero.
                
    Returns:
        list: Lista de palabras que sea más larga que n.
    
        
        """
    texto = cadena.split()
    return list(filter(lambda palabra: len(palabra) > n, texto))

colores = "amarillo rojo azul negro rosa"
resultado = palabras_mas_largas(colores, 4)
print(resultado)

#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
#corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce
def lista_digitos(digitos):
     """Devuelve un número de una lista de dígitos.
    Args:
        digitos (list): Lista de dígitos.
            
                    
    Returns:
        int: Número entero.
        
            
        """
     
     resultado = reduce(lambda acumulado, x: acumulado * 10 + x, digitos) 
     return resultado

print(lista_digitos([5, 7, 2]))

#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
#90. Usa la función filter()

def estudiantes_aprobados(estudiantes):

    """Devuelve a los estudiantes con una calificación mayor o igual a 90.
        Args:
            estudiantes (list): Lista de estudiantes.
                
                        
        Returns:
            list: Lista de diccionarios de los estudiantes con calificaciones mayor o igual a 90.
            
                
        """

    

    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))

estudiantes = [
    {"nombre": "Paula", "edad": 28, "calificacion": 92},
    {"nombre": "Antonio", "edad": 25, "calificacion": 82},
    {"nombre": "Javier", "edad": 30, "calificacion": 95},
    {"nombre": "Laura", "edad": 32, "calificacion": 80},

    ]

print(estudiantes_aprobados(estudiantes))

#19. Crea una función lambda que filtre los números impares de una lista dada.  
      
filtrar_impares = lambda x: x % 2 != 0
numeros = [5, 7, 10, 2, 4, 3, 6]
resultado = list(filter(filtrar_impares, numeros))
print(resultado)

#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
#filter()
def solo_enteros(lista_mixta):
    """Devuelve una lista sólo con los valores int de una lista mixta.
    Args:
        lista_mixta (list): Lista con elementos tipo integer y string.
    Returns:
        list: Nueva lista sólo con los valores int.
    """
    return list(filter(lambda x: isinstance(x, int), lista_mixta))
print(solo_enteros([1, "dos", 3, "cuatro", 5, "seis"]))

#21. Crea una función que calcule el cubo de un número dado mediante una función lambda.
cubo = lambda x: x ** 3
numero = 3
print(cubo(numero))

#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

from functools import reduce

def producto_total(numeros):
    """Calcula el producto total de los valores de una lista numérica.
    Args:
        numeros (list): lista numérica.
    Returns:
        int: producto total de los valores de la lista.
    """
    return reduce(lambda x, y: x * y, numeros)
print(producto_total([1, 3, 5, 8, 12]))

#23. Concatena una lista de palabras.Usa la función reduce() .

from functools import reduce

def concatenar_palabras(palabras):
    """Concatena una lista de palabras en una sola cadena.
    Args:
        palabras (list): Lista de palabras.
    Returns:
        str: Cadena resultante de la concatenación de las palabras.
    

    """
    return reduce(lambda acumulado, palabra: acumulado + " " + palabra, palabras)
print(concatenar_palabras(["Hola", "mundo", "esto", "es", "una", "prueba"]))

#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce

def diferencia_total(numeros):
    """Calcula la diferencia total en los valores de una lista.
    Args:
        numeros (list): Lista de números.
    Returns:
        int: Diferencia total de los valores de la lista.
    """
    return reduce(lambda x, y: x - y, numeros)

print(diferencia_total([100, 20, 30, 10]))

#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(cadena):
    """Cuenta el número de caracteres en una cadena de texto.
    Args:
        cadena (str): Cadena de texto.
    Returns:
        int: Número de caracteres en la cadena.
    """
    return len(cadena)

print(contar_caracteres("Hola Mundo"))

#26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda x, y: x % y
num1 = 10
num2 = 3
print(resto(num1, num2))

#27. Crea una función que calcule el promedio de una lista de números.

def promedio_lista(numeros):
    """Calcula el promedio de una lista de numeros.
    Args:
        numeros (list): Lista de números.
    Returns:
        float: Promedio de los números en la lista.
    """
    return sum(numeros) / len(numeros)

print(promedio_lista([10, 30, 60, 40, 50]))


  



     
    
    
    





