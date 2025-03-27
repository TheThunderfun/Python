print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
input_tip = int(input("What percentage tip would you like to give 10 , 12 or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = input_tip / 100 * total_bill + total_bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
# Output: Welcome to the tip calculator.
# What was the total bill? $124.56  