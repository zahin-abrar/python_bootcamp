"""
You're creating a tea menu board.
Each item must be numbered.
Task:
Use enumerate() to print menu items with numbers.
"""
menu = ["Green", "Lemon", "Spiced", "Mint"]

for idx, m in enumerate(menu, start=1): #will create a tuple (idx, m) for each item in the menu list
    print(f"{idx}: Menu item is {m} chai")