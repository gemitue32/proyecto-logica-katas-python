## Proyecto Lógica: Katas de Python

Proyecto final del módulo de Python del curso de Data Analytics en The Power.
Consiste en resolver 41 katas (ejercicios prácticos) que cubren tipos de datos,
estructuras de datos, condicionales, bucles, funciones (map/filter/reduce/lambda),
clases y buenas prácticas.

## Estructura del repositorio

- `katas.py`: contiene todos los ejercicios resueltos. Cada uno va precedido de
  un comentario con el enunciado original.
- `README.md`: este archivo, con la documentación del proyecto.

## Pasos seguidos

1. Creación del repositorio en GitHub (público, con README inicial).
2. Conexión del repositorio con la carpeta local en VS Code (`git init` + `git remote add` + `git pull`).
3. Resolución progresiva de los 41 ejercicios en `katas.py`, documentando cada
   función con docstrings (extensión autoDocstring) y comentando el enunciado
   encima de cada una.
4. Commits regulares a medida que se completan bloques de ejercicios.

## Progreso

- [x] Ejercicios 1-24
- [ ] Ejercicios 25-41

## Dificultades y aprendizajes

- **Ejercicio 16** (palabras más largas que n, con `filter()`): este ejercicio me
  costó bastante. Al principio me confundí con el ejemplo de prueba: usé una
  lista/tupla de palabras en vez de una cadena de texto como pedía el enunciado,
  y por eso `.split()` me daba error. Luego tuve problemas para entender el orden
  de los argumentos dentro de `filter()` — puse `n` donde debía ir la lista de
  palabras, y en el `lambda` intenté "llamar" a la palabra como si fuera una
  función en vez de comparar su longitud con `len()`. Tuve que parar y repasar
  la estructura de `filter(funcion, lista)` paso a paso para entender qué papel
  jugaba cada pieza antes de conseguir que funcionara.

## Cómo ejecutar el código

Desde la terminal, dentro de la carpeta del proyecto:

\`\`\`bash
python katas.py
\`\`\`
