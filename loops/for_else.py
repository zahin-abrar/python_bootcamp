# else is used with for loop. Used as fall back for the loop when no result is found after the loop completes
# for-else runs the else block only if the loop didn't hit  a break.
# Example usage: "You’ve looped through a list of payment attempts. If none failed, you want to print “All Successful.” Where do you write that?"
# In this case, print will be inside else block on the loop because this is where the code will execute only if none of the iterations
# encountered a break statement, indicating that all payment attempts were successful.
# This properly aligns with your goal of printing "All Successful" only after confirming all attempts succeeded.


staff = [("John", 16), ("Jane", 17), ("Bob", 15)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print("No staff member is eligible to manage the staff")