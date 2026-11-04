# Problem Statement

Write a program to compare course schedules represented by strings and tuples, detect overlapping periods, identify unavailable rooms, and validate a proposed timetable. 

# Algorithm

1. Start
2. Set the available rooms and course details.
3. Check each course for an unavailable room.
4. Compare courses for overlapping times on the same day.
5. Display any conflicts, or display that the timetable is valid.
6. Stop

# Flowchart
```mermaid
flowchart TD
    A([Start]) --> B[Check course rooms and times]
    B --> C{Any conflict?}
    C -- Yes --> D[/Display conflicts/]
    C -- No --> E[/Display timetable is valid/]
    D --> F([Stop])
    E --> F
```

# Sample Input

Math, Monday, 9–10, Room 1
Science, Monday, 10–11, Room 1

# Sample Output

Timetable is valid

