age: int = 31
year: int = 2025

add: int = 10 + 5
minus: int = 10 - 3
times: int = 4 * 5
divide: int = 10 // 3
module: int = 10 % 3
pow: int = 2**3

print("=== INTEGERS ===")
print(f"Age: {age}")
print(f"10 // 3 = {divide}")
print(f"10 % 3 = {module}")
print(f"2**3 = {pow}")
print("================")
print("")

price: float = 19.99
temperature: float = -3.5
pi: float = 3.14159

regular_divide: float = 10 / 3

total: float = price * 2
average: float = (10.5 + 20.3 + 15.7) / 3

print("=== FLOATS ===")
print(f"Price: ${price}")
print(f"10 / 3 = {regular_divide}")
print(f"Average: {average}")
print(f"PI with 2 decimals: {pi:.2f}")
print(f"PI with 4 decimals: {pi:.4f}")
print("================")
print("")

name: str = "Lucas"
surname: str = "Cabrera"

full_name: str = name + " " + surname

message: str = """
This is a message
in multiples lines
very useful for large texts
"""

upper_name: str = name.upper()
lower_name: str = name.lower()
clean_name: str = "     Lucas".strip()

print("=== STRINGS ===")
print(f"Full Name: {full_name}")
print(f"Capped Name: {upper_name}")
print(f"Lower Name: {lower_name}")

age_in_5years: int = 31 + 5
print(f"In 5 years I'll have {age_in_5years} old")
print(f"I'm adult? {31 >= 18}")
print("================")
print("")

is_student: bool = True
is_professor: bool = False

is_adult: bool = 31 >= 18
is_under_10: bool = 5 < 10
is_equal: bool = 5 == 5
is_different: bool = 5 != 3

print("=== BOOLEANS ===")
print(f"Is a student?: {is_student}")
print(f"Is an adult?: {is_adult}")
print(f"5 == 5: {is_equal}")
print(f"5 != 3: {is_different}")

have_notebook: bool = True
have_internet: bool = True
can_programming: bool = have_notebook and have_internet

print(f"Can programing?: {can_programming}")
print("================")
print("")

result: None = None
undefined_variable: int | None

print("=== NONE ===")
print(f"Result: {result}")
print(f"Result is None? {result is None}")


def get_age(name: str) -> int | None:
    if name == "Lucas":
        return 31
    return None


age_Lucas = get_age("Lucas")
age_Juan = get_age("Juan")

print(f"Lucas's age: {age_Lucas}")
print(f"Juan's age: {age_Juan}")
print("================")
print("")

print("=== ADVANCE TYPE HINTS ===")
age_or_text: int | str = 31
age_or_text = "treinta y uno"

optional_name: str | None = None
optional_name = "Lucas"

valor: int | float | str = 42
valor = 3.14
valor = "texto"

print(f"Valor can be differents types: {valor}")
print("================")
