class Employee:
    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"


class Manager(Employee):
    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self._salary * 0.1


def show_employees(employees):
    for emp in employees:
        print(emp.get_role(), emp.get_salary())


emp1 = Employee(1000)
emp2 = Manager(2000)

show_employees([emp1, emp2])