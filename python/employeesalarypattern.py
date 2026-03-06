class Employee:
    bonus_rate = 0.1

    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def final_salary(self):
        return self.base_salary + (self.base_salary * Employee.bonus_rate)

    @classmethod
    def update_bonus(cls, new_rate):
        cls.bonus_rate = new_rate

    @staticmethod
    def is_valid_salary(sal):
        return sal > 0

e1 = Employee("Ravi", 50000)
e2 = Employee("Arun", 60000)

print(e1.final_salary())

Employee.update_bonus(0.2)

print(e1.final_salary())