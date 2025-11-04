"""
String Slicing en Python
Extraer partes de strings
"""

texto: str = "Python Programming"
#            0123456789...
#            P y t h o n   P r o g r a m m i n g

# === ÍNDICES BÁSICOS ===
print("=== ÍNDICES ===")
print(f"texto: {texto}")
print(f"texto[0]: {texto[0]}")  # P (primer carácter)
print(f"texto[7]: {texto[7]}")  # P (octavo carácter)
print(f"texto[-1]: {texto[-1]}")  # g (último)
print(f"texto[-2]: {texto[-2]}")  # n (penúltimo)

# === SLICING [inicio:fin] ===
print("\n=== SLICING [inicio:fin] ===")
print(f"texto[0:6]: {texto[0:6]}")  # Python (del 0 al 5, NO incluye 6)
print(f"texto[:6]: {texto[:6]}")  # Python (desde inicio)
print(f"texto[7:]: {texto[7:]}")  # Programming (hasta el final)
print(f"texto[7:14]: {texto[7:14]}")  # Program

# === SLICING CON STEP [inicio:fin:step] ===
print("\n=== SLICING CON STEP ===")
print(f"texto[::2]: {texto[::2]}")  # Pto rgamn (cada 2 caracteres)
print(f"texto[::3]: {texto[::3]}")  # Ph gm (cada 3)
print(f"texto[::-1]: {texto[::-1]}")  # gnimmargorP nohtyP (reverso!)

# === CASOS DE USO PRÁCTICOS ===
print("\n=== CASOS PRÁCTICOS ===")

# Extraer extensión de archivo
archivo: str = "documento.pdf"
extension: str = archivo[-3:]  # Últimos 3 caracteres
print(f"Archivo: {archivo} → Extensión: {extension}")

# Extraer dominio de email
email: str = "lucas@gmail.com"
indice_arroba: int = email.find("@")
dominio: str = email[indice_arroba + 1 :]
print(f"Email: {email} → Dominio: {dominio}")

# Primeras 3 letras de nombre (nickname)
nombre_completo: str = "Lucas Andres"
nickname: str = nombre_completo[:3].upper()
print(f"Nombre: {nombre_completo} → Nickname: {nickname}")

# Ocultar número de tarjeta (mostrar solo últimos 4)
tarjeta: str = "1234567890123456"
oculta: str = "**** **** **** " + tarjeta[-4:]
print(f"Tarjeta: {tarjeta} → Mostrar: {oculta}")
