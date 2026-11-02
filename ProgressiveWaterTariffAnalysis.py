count = int(input("Number of households: "))
fixed_fee = 50

for i in range(count):
    name = input("Household name: ")
    usage = float(input("Water usage: "))

    if usage <= 30:
        bill = usage * 5 + fixed_fee
    elif usage <= 60:
        bill = 30 * 5 + (usage - 30) * 8 + fixed_fee
    else:
        bill = 30 * 5 + 30 * 8 + (usage - 60) * 12 + fixed_fee + 100

    print(name, "usage:", usage, "Bill:", bill)

    if usage > 60:
        print("Excessive usage")