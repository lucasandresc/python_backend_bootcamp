name: str = "Lucas"
age: int = 31
language: str = "Python"
version: str = "3.14"
city: str = "Ushuaia"


def greet(name: str) -> None:
    print(f"Hello, {name}!")
    print(f"Welcome to {language} {version} worlds!")


def show_info(name: str, age: int, language: str) -> None:
    print("\n" + "=" * 50)
    print(f"Student: {name}")
    print(f"City: {city}")
    print(f"Age: {age} old")
    print(f"Learning: {language}")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    greet(name)

    show_info(name, age, language)

    print("Your journey to become a Backend Developer begins NOW!")
