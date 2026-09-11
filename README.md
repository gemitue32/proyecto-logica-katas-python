## Proyecto Lógica: Katas de Python

Proyecto final del módulo de Python del curso de Data Analytics en The Power.
Consiste en resolver 41 katas (ejercicios prácticos) que cubren tipos de datos,
estructuras de datos, condicionales, bucles, funciones (map/filter/reduce/lambda),
clases y buenas prácticas.

**Nota:** la numeración salta del ejercicio 34 al 36 porque así lo indica
el propio enunciado del proyecto (no existe un ejercicio 35).

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

- [x] Ejercicios 1-41

## Dificultades y aprendizajes

- **Ejercicio 36** (clase UsuarioBanco): al reproducir el caso de uso exacto
  del enunciado, detecté una inconsistencia en los números de ejemplo: Bob
  empieza con 50, se le agregan 20 (queda con 70), y después se pide transferir
  80 desde Bob a Alicia — una cantidad mayor de la que Bob tiene disponible.
  Mi método `retirar_dinero` lanza correctamente un `ValueError` en este caso,
  ya que no tiene sentido permitir una transferencia sin saldo suficiente.
  Decidí mantener la validación intacta (en vez de "forzar" que el ejemplo
  funcionara) y capturar el error con `try/except` para que el programa
  gestione el fallo de forma controlada, sin interrumpirse.
  
- **Ejercicio 37** (procesar_texto con *args): fue el ejercicio más complejo
  del proyecto, al combinar varias funciones auxiliares (contar_palabras,
  reemplazar_palabras, eliminar_palabra) con una función controladora que
  decide cuál ejecutar según el valor de `opcion`. Lo más difícil fue entender
  cómo `*args` empaqueta un número variable de argumentos en una tupla, y
  cómo acceder a cada uno con `args[0]`, `args[1]`... según la opción
  necesitara uno o dos datos adicionales.

## Cómo ejecutar el código

Desde la terminal, dentro de la carpeta del proyecto:

\`\`\`bash
python katas.py
\`\`\`
