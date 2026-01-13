import json

with open("students.json", "r") as file:
    students = json.load(file)

for person in students:
    grades = person["grades"]
    person["average"] = sum(grades) / len(grades)

with open("students_with_average.json", "w") as file:
    json.dump(students, file, indent=4)

print("Done")
