class Employee:

    raise_ammount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def pay_raise(self):
        self.pay = self.pay * Employee.raise_ammount

    @classmethod
    def set_raise_ammount(cls, ammount):
        cls.raise_ammount = ammount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)


# emp3_str = 'km-maw-900'
# emp3 = Employee.from_string(emp3_str)
# print(emp3)

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_emp(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_names(self):
        for employee in self.employees:
            print(f'--> {employee.fullname}')

emp1 = Developer('yx', 'tan', 100, 'python')
emp2 = Developer('tulu', 'maw', 500, 'java')
man1 = Manager('Km', 'Maw', 1000, [emp1, emp2])

man1.print_names()