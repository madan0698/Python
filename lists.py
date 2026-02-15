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


# to avoid modifying both we can use copy command

states = ['ka', 'kl', 'tn', 'ap']

south_states = states.copy()    

states.append('Te')

print (f"States ===> {states}")    
print (f"S_states===> {south_states}")

#id 

states = ['ka', 'kl', 'tn', 'ap']

south_states = states.copy()    

states.append('Te')

print (f"States ===> {states} {id(states)}")    
print (f"S_states===> {south_states} {id(south_states)}")