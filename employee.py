"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salaryContract, monthlySalary, hourlyContract, hourlyWage, numberOfHoursWorked, recievesCommission, fixedBonus, fixedBonusAmount, contractCommission, numberOfContractsLanded, commissionPerContract ):
        self.name = name

        self.salaryContract = salaryContract    #True/False
        self.monthlySalary = monthlySalary
        self.hourlyContract = hourlyContract    #True/False
        self.hourlyWage = hourlyWage
        self.numberOfHoursWorked = numberOfHoursWorked

        self.recievesCommission = recievesCommission    #True/False
        self.fixedBonus = fixedBonus    #True/False
        self.fixedBonusAmount = fixedBonusAmount
        self.contractCommission = contractCommission    #True/False
        self.numberOfContractsLanded = numberOfContractsLanded
        self.commissionPerContract = commissionPerContract

    def get_commission(self):
        if self.fixedBonus == True:
                return (self.fixedBonusAmount)
        if self.contractCommission == True:
            return self.numberOfContractsLanded * self.commissionPerContract

    def get_pay(self):
        if self.salaryContract == True:
            if self.recievesCommission == True:
                return (self.monthlySalary + self.get_commission())
            if self.recievesCommission == False:
                return self.monthlySalary

        if self.hourlyContract == True:
            if self.recievesCommission == True:
                return ((self.hourlyWage*self.numberOfHoursWorked) + self.get_commission())
            if self.recievesCommission == False:
                return self.hourlyWage*self.numberOfHoursWorked

    def __str__(self):
            if self.salaryContract == True:
                if self.recievesCommission == True:
                    if self.fixedBonus == True:
                        return (f"{self.name} works on a monthly salary of {self.monthlySalary} and receives a bonus commission of {self.fixedBonusAmount}. Their total pay is {self.get_pay()}." )
                    else:
                        return (f"{self.name} works on a monthly salary of {self.monthlySalary} and receives a commission for {self.numberOfContractsLanded} contract(s) at {self.commissionPerContract}/contract.  Their total pay is {self.get_pay()}.")
                else:
                    return(f"{self.name} works on a monthly salary of {self.monthlySalary}.  Their total pay is {self.get_pay()}.")

            else:
                if self.recievesCommission == True:
                    if self.fixedBonus == True:
                        return (f"{self.name} works on a contract of {self.numberOfHoursWorked} hours at {self.hourlyWage}/hour and receives a bonus commission of {self.fixedBonusAmount}.  Their total pay is {self.get_pay()}.")
                    else:
                        return (f"{self.name} works on a contract of {self.numberOfHoursWorked} hours at {self.hourlyWage}/hour and receives a commission for {self.numberOfContractsLanded} contract(s) at {self.commissionPerContract}/contract.  Their total pay is {self.get_pay()}.")
                else:
                    return (f"{self.name} works on a contract of {self.numberOfHoursWorked} hours at {self.hourlyWage}/hour.  Their total pay is {self.get_pay()}.")

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', True, 4000, False, 0, 0, False, False, 0, False, 0, 0 )
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', False, 0, True, 25, 100, False, False, 0, False, 0, 0)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', True, 3000, False, 0, 0, True, False, 0, True, 4, 200)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', False, 0, True, 25, 150, True, False, 0, True, 3, 220)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, 2000, False, 0, 0, True, True, 1500, False, 0, 0)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', False, 0, True, 30, 120, True, True, 600, False, 0, 0)
