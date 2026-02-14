# how to check particular letter count 

statement = 'IT Defined, located in Bangalore, is a leading training provider offering interact'

print (statement.count('t'))  #we will get count of small letter only, it is case sensitive 

print (statement.count('T'))   #we will get count of upper letter only, it is case sensitive

print (statement)  #it will not be modified


#split function 

statement = 'abcxefgxklm'

statement2= statement.split ('x')

print (statement2)


