enue = float(input("Venue cost: "))
equipment = float(input("Equipment cost: "))
catering_per_person = float(input("Catering cost per participant: "))
transport = float(input("Transport cost: "))
certificate_per_person = float(input("Certificate cost per participant: "))
sponsorship = float(input("Sponsorship amount: "))
contribution = float(input("Contribution per participant: "))

fixed_costs = venue + equipment + transport
cost_per_person = catering_per_person + certificate_per_person

shortfall = max(0, fixed_costs - sponsorship)
break_even_count = 0

if contribution > cost_per_person:
    break_even_count = (shortfall // (contribution - cost_per_person)) + 1
elif shortfall > 0:
    print("Break-even is not possible with this contribution.")

print("\nEVENT FINANCIAL SUMMARY")
print("=======================")
print(f"Fixed costs: {fixed_costs:.2f}")
print(f"Cost per participant: {cost_per_person:.2f}")
print(f"Sponsorship shortfall: {shortfall:.2f}")

if contribution > cost_per_person or shortfall == 0:
    print(f"Minimum participants to break even: {break_even_count}")
