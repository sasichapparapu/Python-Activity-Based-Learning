attended = int(input("Classes attended so far: "))
held = int(input("Classes held so far: "))
threshold = float(input("Required attendance percentage: "))
future_classes = int(input("Upcoming classes: "))

current = attended / held * 100
print(f"\nCurrent attendance: {current:.1f}%")

for missed in range(future_classes + 1):
    attended_future = attended + future_classes - missed
    total_future = held + future_classes
    percentage = attended_future / total_future * 100

    print(f"If you miss {missed} classes: {percentage:.1f}%")

needed = 0
while (attended + needed) / (held + needed) * 100 < threshold:
    needed += 1

print("Consecutive classes to attend to reach threshold:", needed)
