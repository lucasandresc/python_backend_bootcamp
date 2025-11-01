# 1- Real information Variables
name: str = "Lucas"
age: int = 31
height: float = 1.68
is_developer: bool = True

# 2- Calculate Year of birth
actual_year: int = 2025
birth_year: int = 2025 - age

# 3- Calculate your age in days
days_in_year: int = 365
age_in_days: int = 365 * age

# 4 - Cover message
presentation: str = f"""
Hi, my name is {name}
I'm {age} old (I borned in {birth_year}).
I'm {height}m of height.
I've lived aprox {age_in_days} days.
I'm a programmer? {is_developer}
"""

print("=== INFORMATION ===")
print(presentation)
