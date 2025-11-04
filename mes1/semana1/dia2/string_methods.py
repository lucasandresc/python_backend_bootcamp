"""
String Methods en Python 3.14
Manipulación profesional de texto
"""

nombre: str = "Lucas Andres"

# === CASE CONVERSION (cambiar mayúsculas/minúsculas) ===
print("=== CASE CONVERSION ===")
print(f"Original: {nombre}")
print(f"upper(): {nombre.upper()}")      # LUCAS ANDRES
print(f"lower(): {nombre.lower()}")      # lucas andres
print(f"title(): {nombre.title()}")      # Lucas Andres (cada palabra)
print(f"capitalize(): {nombre.capitalize()}")  # Lucas andres (solo primera)
print(f"swapcase(): {nombre.swapcase()}")     # lUCAS aNDRES (invierte)

# === WHITESPACE REMOVAL (quitar espacios) ===
print("\n=== WHITESPACE REMOVAL ===")
texto_sucio: str = "   hola mundo   "
print(f"Original: '{texto_sucio}'")
print(f"strip(): '{texto_sucio.strip()}'")    # 'hola mundo' (ambos lados)
print(f"lstrip(): '{texto_sucio.lstrip()}'")  # 'hola mundo   ' (izquierda)
print(f"rstrip(): '{texto_sucio.rstrip()}'")  # '   hola mundo' (derecha)

# === BÚSQUEDA (search) ===
print("\n=== BÚSQUEDA ===")
frase: str = "Python es genial"
print(f"Frase: {frase}")
print(f"'Python' in frase: {'Python' in frase}")  # True
print(f"'Java' in frase: {'Java' in frase}")      # False
print(f"startswith('Python'): {frase.startswith('Python')}")  # True
print(f"endswith('genial'): {frase.endswith('genial')}")      # True
print(f"find('es'): {frase.find('es')}")          # 7 (índice donde empieza)
print(f"find('Java'): {frase.find('Java')}")      # -1 (no encontrado)
print(f"count('e'): {frase.count('e')}")          # 2 (aparece 2 veces)

# === REEMPLAZO (replace) ===
print("\n=== REEMPLAZO ===")
texto: str = "Me gusta Java"
nuevo: str = texto.replace("Java", "Python")
print(f"Original: {texto}")
print(f"Reemplazado: {nuevo}")  # Me gusta Python

# === SPLIT & JOIN ===
print("\n=== SPLIT & JOIN ===")
csv: str = "Lucas,31,Argentina"
partes: list[str] = csv.split(",")  # Convierte a lista
print(f"CSV: {csv}")
print(f"split(','): {partes}")  # ['Lucas', '31', 'Argentina']

# JOIN (inverso de split)
lista: list[str] = ["Python", "es", "genial"]
frase_unida: str = " ".join(lista)
print(f"\nLista: {lista}")
print(f"join(' '): {frase_unida}")  # Python es genial

# === VALIDACIÓN ===
print("\n=== VALIDACIÓN ===")
numero: str = "12345"
texto_alfa: str = "Python"
alfanumerico: str = "Python3"

print(f"'{numero}'.isdigit(): {numero.isdigit()}")        # True
print(f"'{texto_alfa}'.isalpha(): {texto_alfa.isalpha()}")    # True
print(f"'{alfanumerico}'.isalnum(): {alfanumerico.isalnum()}")  # True
print(f"'{texto_alfa}'.isupper(): {texto_alfa.isupper()}")    # False
print(f"'{texto_alfa}'.islower(): {texto_alfa.islower()}")    # False

# === PADDING (rellenar) ===
print("\n=== PADDING ===")
num: str = "42"
print(f"zfill(5): {num.zfill(5)}")    # 00042 (rellena con ceros)
print(f"center(10, '*'): {num.center(10, '*')}")  # ****42****
print(f"ljust(10, '-'): {num.ljust(10, '-')}")    # 42--------
print(f"rjust(10, '-'): {num.rjust(10, '-')}")    # --------42
