from datetime import datetime

"""F-strings avanzados en Python 3.14"""

# === FORMATEO DE NÚMEROS ===

precio: float = 1234.5678

# Redondear decimales
print(f"Precio: ${precio:.2f}")  # $1234.57

# Separador de miles
print(f"Precio: ${precio:,.2f}")  # $1,234.57

# Ancho fijo (padding)
print(f"Precio: ${precio:>10.2f}")  # $   1234.57 (10 caracteres de ancho)

# Porcentajes
tasa: float = 0.175
print(f"Tasa: {tasa:.1%}")  # 17.5%

# Notación científica
grande: float = 1234567890
print(f"Grande: {grande:.2e}")  # 1.23e+09

print("\n" + "=" * 50 + "\n")

# === ALINEACIÓN DE TEXTO ===

nombre: str = "Lucas"

# Izquierda (default)
print(f"|{nombre:<20}|")  # |Lucas               |

# Derecha
print(f"|{nombre:>20}|")  # |               Lucas|

# Centro
print(f"|{nombre:^20}|")  # |       Lucas        |

# Con carácter de relleno
print(f"|{nombre:*^20}|")  # |*******Lucas********|

print("\n" + "=" * 50 + "\n")

# === EXPRESIONES DENTRO DE F-STRINGS ===

edad: int = 31

# Operaciones matemáticas
print(f"En 5 años tendré {edad + 5} años")

# Condicionales (ternary operator)
print(f"Soy {'mayor' if edad >= 18 else 'menor'} de edad")

# Llamadas a funciones
nombre_completo: str = "lucas andres"
print(f"Nombre: {nombre_completo.title()}")  # Lucas Andres

# Métodos de strings
texto: str = "  hola  "
print(f"Limpio: '{texto.strip()}'")  # 'hola'

print("\n" + "=" * 50 + "\n")

# === DEBUGGING CON F-STRINGS (Python 3.8+) ===

x: int = 10
y: int = 20

# El = al final muestra variable + valor
print(f"{x=}")  # x=10
print(f"{y=}")  # y=20
print(f"{x + y=}")  # x + y=30

# Súper útil para debugging
resultado: int = x * y + 5
print(f"{resultado=}")  # resultado=205

print("\n" + "=" * 50 + "\n")

# === FORMATO DE FECHAS (con datetime) ===


ahora: datetime = datetime.now()

print(f"Fecha completa: {ahora}")
print(f"Solo fecha: {ahora:%Y-%m-%d}")  # 2025-01-30
print(f"Solo hora: {ahora:%H:%M:%S}")  # 19:11:30
print(f"Formato custom: {ahora:%d de %B, %Y}")  # 30 de January, 2025

print("\n" + "=" * 50 + "\n")

# === NÚMEROS BINARIOS, OCTALES, HEXADECIMALES ===

numero: int = 42

print(f"Decimal: {numero}")  # 42
print(f"Binario: {numero:b}")  # 101010
print(f"Octal: {numero:o}")  # 52
print(f"Hex: {numero:x}")  # 2a
print(f"Hex (upper): {numero:X}")  # 2A
