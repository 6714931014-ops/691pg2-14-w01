from Tax import Tax


class Staff:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary


    def yearIncome(self):
        return self.salary * 12


    def calculateTax(self, income):
        return Tax.calculateTax(income)


    def __str__(self) -> str:
        return f"{self.name} Salary: {self.salary} Tax: {self.calculateTax(self.yearIncome())}"
