class Employee:
    #class variable
    raise_perc = 0
    count = 0

    #init method also known as constructor
    def __init__(self, First, Last, Pay):
        self.First = First
        self.Last = Last
        self.Pay = Pay
        self.email = First + '.' + Last + '@surabhi.com'
        #set method call inside init method
        self.setEmployeeRaisePerc()
        #Counting total Employees
        Employee.count += 1

    #class methods
    def getEmployeeFullName(self):
        return self.First + ' ' + self.Last

    def setEmployeeRaisePerc(self):
        if self.Pay <= 50000:
            self.raise_perc = 1.10
        elif self.Pay > 50000:
            self.raise_perc = 1.07
        print "Raise Percentage:" , self.raise_perc

    def getEmployeeRaisePerc(self):
        return self.raise_perc

#main method
def main():
    #class objects
    emp1 = Employee('Sonish','Balan', 50000)
    emp2 = Employee('Sruthi','Arambachalil', 70000)

    #class method calls
    #emp1.setEmployeeRaisePerc()
    #emp2.setEmployeeRaisePerc()

    print "Employee full name:" , emp1.getEmployeeFullName()

    #printing class object contents
    print emp1.__dict__
    print emp2.__dict__

    print "Total Employees:" , Employee.count

    print "New Salary:" , emp1.Pay*emp1.raise_perc
    print "New Salary of "+emp2.getEmployeeFullName()+' is ' , emp2.Pay*emp2.raise_perc

#Run main method if run this python file directly
if __name__ == '__main__':
    main()
