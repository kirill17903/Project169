class Student:
    def __init__(self, name, age, grades: list[float]):
        self.name = name
        self.age = age
        self.grades = grades

def get_avg_grades(student):
    return sum(student.grades) / len(student.grades)

s1 = Student("Анна", 20, [4.56, 5.0, 4.92, 3.43])
s2 = Student("Влад", 21, [4.76, 4.66, 4.9, 3.33])
s3 = Student("Дима", 19, [4.56, 5.0, 4.9, 4.43])

students = [s1, s2, s3]

for s in students:
    avg = get_avg_grades(s)
    print(f"{s.name}: средний балл = {avg:.2f}")

print()

top = [s for s in students if get_avg_grades(s) > 4.1]
print("Студенты с баллом > 4.1:")
for s in top:
    print(f"{s.name} - {get_avg_grades(s):.2f}")