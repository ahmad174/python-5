class Employee:
    def __init__(self,number,name,address,salary,jobTitle):
        self.number = int(number)
        self.__name = str(name)
        self.__address = str(address)
        self.__salary = float(salary)
        self.__jobTitle = str(jobTitle)
        

    def getName(self):
        return self.__name


    def getAddress(self):
        return self.__address


    def getSalary(self):
        return self.__salary

    def getJobTitle(self):
        return self.__jobTitle


    def __del__(self):
        print ( self.__name ,' has been deleted ' )

    




    def first_function(self):
        print('Employee' + str(self.number),'Information:')
        print('     Number' + str(self.number))
        print('     Name' + str(self.__name))
        print('     Address' + str(self.__address))
        print('     Salary' + str(self.__salary))
        print('     Job Title' + str(self.__jobTitle))



    def second_function(self):
        print('Employee' + str(self.number) + 'Information:' + ' Number' + str(self.number) + ' Name' + str(self.__name)+' Address' + str(self.__address)+' Salary' + str(self.__salary) + ' Job Title' + str(self.__jobTitle))



    def setAddress(self, address):
        self.__address = str(address)
            



Employee1 = Employee(1,"Mohammad Khalid","(Amman , Jordan)",500,"Consultant")  
Employee2 = Employee(2,"Hala Rana","(Aqaba/Jordan)",750,"Manager")






Employee1.setAddress('USA')
print('Employee1 New Address:', Employee1.getAddress(), end='\n\n') 




del Employee1
del Employee2

class person:
    def say_hello(self):
        print('Hello')

p = person()
p.say_hello()








