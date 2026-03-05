users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"}
]

discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0,0))
    """
    The selected code retrieves discount information from the `discounts` dictionary based on the user's coupon code:

    ```python
    percent, fixed = discounts.get(user["coupon"], (0,0))
    ```
    
    ## Breakdown:
    
    1. **`discounts.get(user["coupon"], (0,0))`**:
       - Uses the `.get()` method to safely retrieve a value from the `discounts` dictionary
       - The key is `user["coupon"]` (e.g., "P20", "F10", or "P50")
       - If the coupon exists, it returns the corresponding tuple (e.g., `(0.2, 0)` for "P20")
       - If the coupon doesn't exist, it returns the default value `(0, 0)` instead of raising a KeyError
    
    2. **Tuple Unpacking**:
       - The returned tuple is unpacked into two variables:
         - `percent`: The percentage discount (as a decimal, e.g., 0.2 = 20%)
         - `fixed`: The fixed amount discount (e.g., 10 for BDT 10 off)
    
    ## Example:
    - For a user with coupon "P20": `percent = 0.2`, `fixed = 0`
    - For a user with coupon "P50": `percent = 0`, `fixed = 10`
    - For a user with an invalid coupon: `percent = 0`, `fixed = 0` (default)
    
    This approach prevents the program from crashing if an invalid coupon code is encountered.
    """
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount for next visit of BDT {discount}")