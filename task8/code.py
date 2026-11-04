courses = [
    ("Math", "Monday", 9, 10, "Room 1"),
    ("Science", "Monday", 10, 11, "Room 1"),
]

rooms = ["Room 1", "Room 2"]
conflict = False

for i in range(len(courses)):
    name1, day1, start1, end1, room1 = courses[i]

    if room1 not in rooms:
        print(name1, "uses an unavailable room")
        conflict = True

    for j in range(i + 1, len(courses)):
        name2, day2, start2, end2, room2 = courses[j]

        if day1 == day2 and start1 < end2 and start2 < end1:
            print(name1, "conflicts with", name2)
            conflict = True

if not conflict:
    print("Timetable is valid")
