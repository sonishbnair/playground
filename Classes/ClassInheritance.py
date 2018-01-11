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

class Developer(Employee):
    raise_perc = 2.0

    def __init__(self, First, Last, Pay, Prog_lang):
        super(Developer, self).__init__(First, Last, Pay)
        self.Prog_lang=Prog_lang

#main method
def main():

    emp1 = Developer('Sonish','Balan', 70000, 'Python')
    print emp1.getEmployeeFullName, "," , emp1.Prog_lang

    #Print class defenition
    #print(help(Developer))

    #Regular method vs class method
    # emp1 = Developer('Sonish','Balan', 70000)
    # print emp1.getEmployeeFullName() ," Raise % ", emp1.getEmployeeRaisePerc()
    # emp1.setEmployeeRaisePerc()
    # print emp1.getEmployeeFullName() ," Raise % ", emp1.getEmployeeRaisePerc()
    # emp1.setRaisePerc(3.0)
    # print emp1.getEmployeeFullName() ," Raise % ", emp1.getEmployeeRaisePerc()
    #
    # emp2 = Developer('Sruthi','Nair', 5000)
    # print emp2.getEmployeeFullName() ," Raise % ", emp2.getEmployeeRaisePerc()


#Run main method if run this python file directly
if __name__ == '__main__':
    main()
