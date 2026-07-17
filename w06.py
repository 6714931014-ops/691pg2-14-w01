from Tax import Tax
from Staff import Staff
from Department import Department


staff1 = Staff("Alex", 45000)
staff2 = Staff("Michael", 60000)
staff3 = Staff("Charlie", 87000)
staff4 = Staff("Dylan", 100000)
staff5 = Staff("Joe", 150000)


Department = Department()


Department.addStaff(staff1)
Department.addStaff(staff2)
Department.addStaff(staff3)
Department.addStaff(staff4)
Department.addStaff(staff5)


Department.displayResults()
