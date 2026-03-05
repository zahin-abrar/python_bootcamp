value = 13

if remainder := value % 5: # := assigns values to variables as part of a larger expression
    print(f"Not divisible, remainder is {remainder}")

available_sizes = ["small", "medium", "large"]

if(requested_size := input("Enter your coffee cup size: ")) in available_sizes:
    print(f"Serving {requested_size} cup of coffee")
else:
    print(f"size is unavailable - {requested_size}")