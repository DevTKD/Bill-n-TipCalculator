bill_amount = float(input("Enter Bill Total: $ "))
tip_percentage = int(
    input("Enter tip amount in percentage (e.g. For 15%, enter 15): "))

tip_amount = (bill_amount * tip_percentage) / 100

total_bill = bill_amount + tip_amount

print(f"The total tip is: ${tip_amount: .2f}")
print(f"The total bill including tip is: ${total_bill: .2f}")


tip_split = int(input("Split the bill how many ways: "))

individual_bill = total_bill / tip_split
print(f"Your individual bill is ${individual_bill: .2f} including tip!")
