# data1 = []

# print(data1)
# print(type(data1))

# data1 = list ("chitradurga")

# print (data1)

# data1 = ['a'] * 4

# print(data1)

# states = ["ka", "kr", "dl", "hr"]

# states.append("ap")          # append means adding extra element

# print (states)

# states = ['KA']

# states.extend(['KE'])           # extend will give output in one line 

# print(states)



# states = ['ka', 'kl', 'tn', 'mh']

# states.insert(2,'ap')                 # insert command is used to insert the elemnts to the position by giving the position where we wants to  insert

# print (states)



# states = ['ka', 'kl', 'tn', 'mh']

# states.remove('tn')                # remove command will remove element perticularly

# print (states) 



# states = ['ka', 'kl', 'tn', 'mh']

# states.clear()            # clear command will remove everything

# print (states) 



# states = ['ka', 'kl', 'tn', 'ap']

# south_states = states       

# states.append('Te')

# print (f"States ===> {states}")    #fcommand passing the value dynamically
# print (f"S_states===> {south_states}")


# #to avoid modifying both we can use copy command

# states = ['ka', 'kl', 'tn', 'ap']

# south_states = states.copy()    

# states.append('Te')

# print (f"States ===> {states}")    
# print (f"S_states===> {south_states}")

# #id 

# states = ['ka', 'kl', 'tn', 'ap']

# south_states = states.copy()    

# states.append('Te')

# print (f"States ===> {states} {id(states)}")    
# print (f"S_states===> {south_states} {id(south_states)}")


# states = [["ka", "kl", "tn", "ap"], ["mp", "hr", "up", "dl"]]

# n_states = states           #n_states = states.copy()

# print (f"states id===> {id(states)}") 
# print (f"northstates id===> {id(n_states)}")

# states = [["ka", "kl", "tn", "ap"], ["mp", "hr", "up", "dl"]]

# n_states = states[1]

# print (f"states ===> {(states)}") 
# print (f"northstates ===> {(n_states)}")


# #importent
# import copy 

# states = [["kA", "AP"], ["HR", "DL"]]

# n_states = copy.deepcopy(states)

# states[0].append(123)

# print (f"states ===> {states}")
# print (f"northstates ===> {n_states}")


# str1 = "IT Defined, located in Bangalore, is a leading training provider offering interactive courses"

# # str1= list(str1)           #it will list the one by one characters           
# str1= str1.split()          #it will split words by words      

# print (str1)


#how to convert a list into a string we have to use join

# str1 = "IT Defined, located in Bangalore, is a leading training provider offering interactive courses"

# str2lst= str1.split()

# print(str2lst) 

# lst1 = ', ' .join(str2lst) 

# print(lst1)


# lst1= [11, 22, 33, 44, 55, 66, 77, 88, 99]
# lst1.sort(reverse=True)
# print(lst1)

# # important 
# lst1 = ["java-11", "java-22", "java-33"]

# splitdata = lst1[0].split('java')[1]

# splitdata = splitdata.zfill(4)

# joineddata = f'java{splitdata}'

# print(joineddata)
