"""
A program which is useful to clean usernames

"""

print("=== NAME FORMATTER ===")
full_name: str = input("Enter your full name: ")
split_name: list[str] = full_name.split()
new_full_name: str = " ".join(split_name).title().strip()
first_name: str = split_name[0]
second_name: str = split_name[1]

username: str = first_name[:3].lower() + second_name[:3].lower()

initials: str = f"{first_name[0].upper()}. {second_name[0].upper()}"

print("--- RESULT ---")
print(f"Original entered name: {full_name}")
print(f"Clean Name: {new_full_name}")
print(f"First Name: {first_name.title()}")
print(f"Last Name: {second_name.title()}")
print(f"Username: {username}")
print(f"Email: {username}@company.com")
print(f"Initials: {initials}.")
