"""
Tip calculator for a restaurant or any place whose serves food
"""

print("\n" + "=" * 50)
print("=== TIP CALCULATOR ===")
print("=" * 50)

ticket: float = float(input("Total of dinner: "))
tip_percent: int = int(input("Ask for percentage (5, 10, 15, 20): "))
input_customers: int = int(input("How many customers were: "))

tip: float = ticket * (tip_percent / 100)
total_ticket: float = ticket + tip
per_customer: float = total_ticket / input_customers

print("--- SUMMARIZE ---")
print(f"Ticket: ${ticket:.2f}")
print(f"Tip (%{tip_percent}): ${tip:.2f}")
print(f"Total ticket: ${total_ticket:.2f}")
print(f"Per customer: ${per_customer:.2f}")
print("--------------------")
