from Tax import Tax
from Staff import Staff


class Department:
    def __init__(self, name=None) -> None:
        self.name = name
        self.staffs = []


    def addStaff(self, staff):
        self.staffs.append(staff)


    def totalincome(self):
        total_income = 0

        for staff in self.staffs:
            total_income += staff.yearIncome()

        return total_income


    def totaltax(self):
        total_tax = 0

        for staff in self.staffs:
            total_tax += staff.calculateTax(staff.yearIncome())

        return total_tax


    def incomeaverage(self):
        income_average = self.totalincome() / len(self.staffs)

        return income_average


    def taxaverage(self):
        tax_average = self.totaltax() / len(self.staffs)

        return tax_average


    def displayResults(self):
        if self.name:
            print(f"Department: {self.name}")

        total_income = self.totalincome()
        income_average = self.incomeaverage()
        total_tax = self.totaltax()
        tax_average = self.taxaverage()

        print(f"Total Income  {total_income} Average Income  {income_average} ")
        print(f"Total Tax {total_tax} Average Tax : {tax_average} ")
        for staff in self.staffs:
            print(f"{staff.name} - Annual Income: {staff.yearIncome()} Baht - Tax to Pay: {staff.calculateTax(staff.yearIncome())} Baht")