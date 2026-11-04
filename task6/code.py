vehicle = input("Vehicle type (car/bike): ").lower()
entry = int(input("Entry hour (0-23): "))
exit = int(input("Exit hour (0-23): "))

if entry < 0 or entry > 23 or exit < 0 or exit > 23:
    print("Invalid time")
else:
    hours = (exit - entry) % 24
    hours = max(1, hours)

    rates = {"car": 50, "bike": 20}

    if vehicle not in rates:
        print("Invalid vehicle type")
    else:
        fee = min(hours * rates[vehicle], 300)
        print("Parking hours:", hours)
        print("Parking fee:", fee)
