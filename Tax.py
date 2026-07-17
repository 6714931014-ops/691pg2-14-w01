class Tax:
    @staticmethod
    def calculateTax(income):
        tax = 0
        if income < 150000:
            tax = 0
        elif income < 300000:
            tax = (income - 150000) * 0.05
        elif income < 500000:
            tax = (income - 300000) * 0.1 + 7500
        elif income < 750000:
            tax = (income - 500000) * 0.15 + 27500
        elif income < 1000000:
            tax = (income - 750000) * 0.2 + 65000 
        elif income < 2000000:
            tax = (income - 1000000) * 0.25 +  115000 
        elif income < 5000000:
            tax = (income - 2000000) * 0.3 + 365000
        else: 
            tax = (income - 5000000) * 0.35 + 1265000           
   
        return tax
