# def greatuser(x):     # greatuser(x='User')
#     print(f"Hello {x}, welcome to IT Defined")  
#     print("please checkout the courses once\n")

# name = "Madan"  
# greatuser(name)


# name = "Harish"
# greatuser(name)


# name = "Nithin"
# greatuser(name)


# def addNum(num1, num2, num3):
#     out= num1 + num2 + num3
#     print(f"the output of 3 numbers {num1} , {num2} and {num3} is {out}")

# addNum(10, 40)
# addNum(1, 111)
# addNum(80, 40)
# addNum(10, 100)
# addNum(101, 1000, 150)

# def addSeveralNumbers(numbers):
#     out = 0
#     for i in numbers:
#         out += i     # out = out + i

#     print(f"output of number {out}")

# addSeveralNumbers([1 ,5 ,15 ,25 ])

# def addSeveralNumbers(*numbers):                      # single * will give output in tuple formet
#     print(numbers)
#     print(type(numbers))

# addSeveralNumbers(1 ,5 ,15 ,25 )


# def greetUser(name, age, place):
#     print(f"my name is {name}, im {age} years old, basically im from {place}")

# greetUser("Madan", 27, "Chitradurga")
# greetUser("Nikil", 28, "Bengaluru")
# greetUser("Ranjith", 31, "Delhi")
# greetUser("Ajith", 27, "Chitradurga")


   #written statements
# def greetuser(**data):              #** will give output as dictionary formet
#     print(data)

# greetuser(first_name='virat', age= 36, city='Bengaluru')


# def carinfo(**data):
#     print(data)
#     print(type(data))

# carinfo(company='Tata', color= 'Grey', fuel= ['CNG', 'PETROL'])


# def factorialNumber(num):
#     out = 1
#     for i in range(1,num+1):
#         out *= i
#     print(out)

# factorialNumber(5)
    
# def factorialNumber(num):
#     out1 = 1
#     for i in range(1,num+1):
#         out1 *= i

#     print(out1)
#     return 1

# out2= factorialNumber(5)       #return value of factorialnumber(5) will be 1

# out2= out2 + 10

# print(out2)


# num1 = 10

# def someNum():
#     num1 = 300
#     print(f"insidefun ==> {num1}")

# someNum()
# print(f"outsidefun ==> {num1}")



# def someNum1():
#     num1 = 300
#     print(f"insidefun ==> {num1}")

# def someNum2():
#     print(f"insidefun ==> {num1}")     # here the value of num1 will be 10

# num1 = 10
# someNum1()
# someNum2()



# def someNum1():
#     num2 = num1 + 300
#     print(f"insidefun ==> {num2}")

# def someNum2():
#     print(f"insidefun ==> {num1}")     

# num1 = 10
# someNum1()
# someNum2()

# in this way  we can execute the same values by using global variable
# def someNum1():
#     global num1
#     num1 = num1 + 300
#     print(f"insidefun ==> {num1}")

# def someNum2():
#     print(f"insidefun ==> {num1}")     

# num1 = 10
# someNum1()
# someNum2()

# def someNum1():
#     global num1
#     num1 = 20
#     print(f"insidefun ==> {num1}")

# def someNum2():
#     print(f"insidefun ==> {num1}")     

# someNum1()
# someNum2()

def someNum1():
    global num1
    num1 = 20
    print(f"insidefun ==> {num1}")   

someNum1()

print(f"outsidefun ==> {num1}")