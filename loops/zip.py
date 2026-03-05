"""
You're preparing an order summary with customer names and their total bill.
Task:
Use two lists: one for names and one for bills.
Print: "[Name] paid [amount]"
"""

names = ["John", "Alice", "Bob"]
bills = [100, 200, 300]

for name, amount in zip(names, bills): #zip will create a tuple for each name and bill pair
    print(f"{name} paid BDT {amount}")