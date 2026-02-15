# statement1 = "my name is madan" # here the double codes("")/single ('')inside characters is a string
# statement2 = "my name is abhi"
# statement3 = "my name is sanjay"

# statement1 = statement3

# print (statement1)
# print (statement2)
# print (statement3)

#note
#string is a immutable we cann't change the data once it is created.

# \backslash is used to escape the gap between new line to overcome those backslash for 
# every step we use """""" at start and end 
# news= """For decades, several ministries operated from ageing and scattered offices 
# across the Central Vista area, leading to coordination challenges, 
# rising maintenance costs and inefficiencies. 
# The new complexes consolidate these functions into integrated, 
# future-ready facilities aimed at improving coordination and workflow."""

# print (news)

# Single, Double and Triple Quotes
# news = "As the \"BJP-Shiv Sena\" combine inched closer"
# news = 'As the "BJP-Shiv Sena" combine inched closer'
# news = 'As the "BJP-Shiv Sena" \'combine\' inched closer'
# news = '''As the "BJP-Shiv Sena" 'combine' inched closer'''
    
# print(news)



name = "Madan"
place ="chitradurga"


output = name + " - " + place      # here we made concatination, concatination means joining two words

print (output) 

# another way of getting same output

name = "Madan"
place ="chitradurga"

out = f"{name} - {place}"          #f- format string if we use this passing the value dynamically

print (out) 

# *Builtin Methods in String

# upper()
# lower()
# capitalise()
# count('a')
# endswith("closer")
# find("the")


str1 = """IT Defined, located in Bangalore, is a leading training provider offering interactive courses on Cloud
Computing, DevOps, Machine Learning, Data Science, AI, ML, and Embedded Systems. Our mission is to empower
individuals with the knowledge and skills needed to excel in the rapidly evolving IT industry.
With experienced instructors, up-to-date curriculum, and a focus on hands-on learning, we ensure our students 
receive comprehensive training that aligns with industry trends.
We provide an engaging learning environment through a combination of theory, practical exercises, and 
interactive discussions. Our flexible schedules and dedicated support team further enhance the learning experience."""


out = str1.find("to")

print (out)                            # it will give first occurence of the para









# multiple assignment on different variables
# x, y = 10, 30

# print("the value of x", x)    
# print("the value of y", y)

# x, y = y, x

# print("the value of x", x)
# print("the value of y", y)







