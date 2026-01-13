class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def greet(self):
        print(f"Hi, I am {self.name}, ID: {self.student_id}")

person = Person("Someone")
student = Student("Neila", "CS-2406")

person.greet()
student.greet()
