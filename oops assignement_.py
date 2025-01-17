'''Solve the following:
1)Write a program which contains one class named as Demo.
That class contains one class variable as value
There are two instance methods of class as Fun and Gun which displays values of instance variables
Initialise instance variable in constructor by accepting the values from user
After creating the class create the two objects of Demo class as
Obj1 =Demo(11,21)
Obj2 = Demo(51,101)

Now call the instance methods as
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()

2)Write a program which contains one class named as BookStore.
Bookstore class contains two instance variables as Name , Author.
That class contains one class variable as NoofBooks which is initialize to 0
There is one instanace methods of class as Display which displays name, author and number of books.
Initialise instance variable in init method by accepting the values from user as name and author.
Inside init method increment value of NoOfBooks by one.
After creating the class create the two objects of BookStore class as
Obj1=Bookstore(“Linux System Programming”,”Robert Love”)
Obj1.Display()  # Linux System Programming. No of books : 1

Obj2=Bookstore(“C Programming”,”Robert Love”)
Obj2.Display()  # C Programming by Dennis Ritchie. No of books :2

3)Write a program which contains one class named as Circle
Circle class contains three instance variables as Radius,Area ,Circumference.
That class contains one class variable as PI which is initialize to 3.14
Inside init method initialize all instance variables to 0.0
There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference( ),
,Display( )
Accept method will accept value of Radius from user.
CalculateArea () method will calculate area of circle and store it into instance variable Area.
CalculateCircumference () method will calculate circumference of circle and store it into instance variable 
Circumference.
And Display( ) method will display value of all the instance variables as radius , Area , Circumference.
After designing the above class call all instance methods by creating multiple objects

4) Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & Amount.
That Class Contains one class variable as ROI which is initialize to 10.5
Inside init method initialize all name and amount variable by accepting the values from user.
There are four instance methods inside class as Display() , Deposit (), Withdraw( ), CalculateInterest()
Deposit( ) method will accept the amount from user and add that value in class instance variable Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
CalculateInterst() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI
And Display () method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects

5)Write a program which contains one class named as Numbers.
 Arithmetic class contains one instance variables as Value.
 Inside init method initialize that instance variables to the value which is accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfect() , SumFactors(), Factors().
ChkPrime() method will returns true if number is prime otherwise return false
ChkPerfect () method will returns true if number is perfect otherwise return false.
Factors () method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method
As a helper method if required.
After Designing the above class call all instance methods by creating multiple objects.

6)Write a program which contains one class named as Numbers.
 Arithmetic class contains one instance variables as Value1,Value2.
 Inside init method initialize all instance variables to 0.
There are three instance methods inside class as Accept(),Addition(),Subtraction(),Multiplication(),Division().
Accept method will accept value of value1 and value2 from user.
Addition() method will perform addition of Value1 and Value2 and return result.
Subtraction() method will perform subtraction of Value1 and Value2 and return result.
Multiplication() method will perform multiplication of Value1 and Value2 and return result.
Division() method will perform division of Value1 and Value2 and return result.
After Designing the above class call all instance methods by creating multiple objects.

'''
#program-1
class demo:
    value=0
    def __init__(self,*val1):
        self.value=val1
    def Fun(self):
        print(f"The first value is {self.value[0]}")
    def Gun(self):
        print(f"The Second value is {self.value[1]}")
obj=Demo(11,21)
obj2=Demo(51,101)
obj.Fun()
obj.Gun()
obj2.Fun()
obj2.Gun()

#program2
class Bookstore:
    Noofb = 0
    def __init__(self,name,author):
        self.name = name
        self.author=author
        Bookstore.Noofb += 1
    def display(self):
        print(f"{self.name} by {self.author} Noofbooks:{Bookstore.Noofb}")
obj1 = Bookstore("Linux System Programming","Robert Love")
obj2 = Bookstore("C Programming","Robert Love")
obj1.display()
obj2.display()

#program3

class Circle:
    pi = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference_value = 0.0

    def accept(self):
        self.radius = float(input("Enter radius: "))

    def calculatearea(self):
        self.area = Circle.pi * self.radius ** 2  # Calculate and store area

    def calculatecircumference(self):
        self.circumference_value = 2 * Circle.pi * self.radius  # Calculate and store circumference

    def display(self):
        print(f"Radius: {self.radius}")
        print(f"Area of Circle: {self.area}")
        print(f"Circumference of Circle: {self.circumference_value}")

circle = Circle()
circle.accept()
circle.calculatearea()
circle.calculatecircumference()
circle.display()
#Program 4

class BankAccount():
    ROI=10.5
    def __init__(self,Name,Amount):
        self.name=Name
        self.amount=Amount
    def Deposit(self,amount):
        self.amount+=amount
    def Withdrawl(self,amount):
        if amount<=self.amount:
            self.amount-=amount

        else:
            raise "No Sufficient amount in your BankAccount"
        
    def CalculateInterest(self):
        intrest=(self.__class__.ROI/100)*self.amount
        print(f"The intrest would be {intrest}")
    def Display(self):
        print(f"The AccountHolder name is {self.name} and the amount in his bankaccount is {self.amount}")

obj=BankAccount("mukhesh",5000)
obj.Deposit(2000)
obj.Withdrawl(1500)
obj.CalculateInterest()
obj.Display()

#Program 5

class Numbers():
    value=0
    def __init__(self,value):
        Numbers.value=value
    def ChkPrime(self):
        for i in range(2,int(self.value**0.5)+1):
            if self.value%i==0:
                return False
        return True
    def ChkPerfect(self):
        sum_val=1+self.value
        for i in range(2,self.value//2+1):
            if(self.value%i)==0:
                sum_val+=i
        if(sum_val==self.value):
            return True
        return False
    def Factors(self):
        factors=[1]
        for i in range(2,self.value//2+1):
            if(self.value%i)==0:
                factors.append(i)
        factors.append(self.value)
        return factors
    def SumOfFactors(self):
        sum_val=1+self.value
        for i in range(2,self.value//2+1):
            if(self.value%i)==0:
                sum_val+=i
        return sum_val
obj=Numbers(6)
print(obj.ChkPerfect())
print(obj.ChkPrime())
print(obj.SumOfFactors())
print(obj.Factors())

#program 6

class Number2():
    def __init__(self):
        self.val1=0
        self.val2=0
    def Accept(self,val1,val2):
        self.val1=val1
        self.val2=val2
    def Addition(self):
        return self.val1+self.val2
    def Subraction(self):
        return self.val1-self.val2
    def Multiplication(self):
        return self.val1*self.val2
    def Division(self):
        return self.val1/self.val2
obj=Number2()
obj.Accept(8,3)
print(obj.Addition())
print(obj.Subraction())
print(obj.Multiplication())
print(obj.Division())
