bill = float(input("Enter your bill amount: "))

tip_percentage = float(input("Enter tip percentage: "))

tip = bill * (tip_percentage / 100)

total = bill + tip

print(f"Tip amount: {tip:.2f}")
print(f"Total bill: {total:.2f}")

while True:
    people = int(input("How many people are sharing the bill? "))

    if people > 0:
        break

    print("Number of people must be greater than zero.")

per_person = total / people

print(f"Amount per person: {per_person:.2f}")