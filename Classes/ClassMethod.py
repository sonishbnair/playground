import datetime

class Employee:
    #class variable
    raise_perc = 1.0
    count = 0

    #init method also known as constructor
    def __init__(self, First, Last, Pay):
        self.First = First
        self.Last = Last
        self.Pay = Pay
        self.email = First + '.' + Last + '@surabhi.com'
        #set method call inside init method
        #self.setEmployeeRaisePerc()
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

    @classmethod
    def setRaisePerc(cls,perc):
        print "inside setRaisePerc", perc
        cls.raise_perc = perc
        print "inside setRaisePerc", perc , "::", cls.raise_perc

    @staticmethod
    def isWorkDay(day):
        if day.weekday()==5 or day.weekday()==6:
            return false
        return True

#main method
def main():

    #Print class defenition
    #print(help(Employee))

    #class objects
    emp2 = Employee('Sruthi','Arambachalil', 70000)

    print "Base Salary of "+emp2.getEmployeeFullName()+' is ' , emp2.Pay*emp2.raise_perc

    #class method calls
    emp2.setEmployeeRaisePerc()

    print "Total Employees:" , Employee.count

    print "->Current Salary of "+emp2.getEmployeeFullName()+' is ' , emp2.Pay*emp2.raise_perc

    Employee.setRaisePerc(2.0)
    print "-------New Salary of"+emp2.getEmployeeFullName()+' is ' , emp2.Pay*emp2.raise_perc, "--Raise % is:", emp2.getEmployeeRaisePerc()

    #Static method call example
    print "Today is workday? ", Employee.isWorkDay(datetime.date.today())

#Run main method if run this python file directly
if __name__ == '__main__':
    main()
