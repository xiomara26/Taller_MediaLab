# datos_iniciales.py
# Sesión 01 · Taller de Python, extracción de datos e IA generativa (Media Lab PUCP)
#
# Objetivo: organizar los primeros datos de tu caso en listas y diccionarios.
# Pasos: 1) Lee el ejemplo.  2) Reemplaza los datos por los de tu caso.  3) Ejecuta el archivo.
# Todo lo que empieza con # es un comentario: Python lo ignora.

# --- 1. LISTA: colección ordenada (se lee por posición; la primera es la 0) ---
fuentes = ["Fuente A", "Fuente B", "Fuente C"]   # TODO: escribe tus propias fuentes
print("Primera fuente:", fuentes[0])
fuentes.append("Fuente D")                       # agrega un elemento al final
print("Total de fuentes:", len(fuentes))

# --- 2. DICCIONARIO: pares clave-valor (se lee por clave) ---
registro = {
    "nombre": "Dato de ejemplo",   # TODO: cambia las claves y los valores según tu especialidad
    "fecha": "2026-01-01",
    "fuente": "https://ejemplo.pe",
}
print("Nombre:", registro["nombre"])
registro["nota"] = "agregado después"            # agrega una clave nueva

# --- 3. LISTA DE DICCIONARIOS: una tabla (cada diccionario es una fila) ---
registros = [
    {"nombre": "Dato 1", "fecha": "2026-01-01", "fuente": "https://ejemplo.pe/1"},
    {"nombre": "Dato 2", "fecha": "2026-01-02", "fuente": "https://ejemplo.pe/2"},
    {"nombre": "Dato 3", "fecha": "2026-01-03", "fuente": "https://ejemplo.pe/3"},
]
# TODO: deja entre 3 y 5 registros REALES de tu caso, con su fuente.
print("Cantidad de registros:", len(registros))
print("Segundo registro:", registros[1]["nombre"])

# --- 4. Comprobación ---
# Si ves los mensajes sin errores, tu archivo funciona.
# Si aparece un error, lee la última línea: IndexError (posición que no existe),
# KeyError (clave que no existe) o SyntaxError (falta una coma, comilla o llave).
