# x = (10, 20)

# print(hash(x))    #in this way we can check hashable or not

# # #syntax
# # data= {
# #     key:value
# # }


# student_data= {
#     "Name": "Madan",
#     "Name": "Abhi"
# }

# print(student_data)         #it will print last updated value, Dictionary is also ordered

student_data= {
    "Name": "Madan",
    "Age": 27, 
    "Skills": ["cricket","vollyball"],
    "Parents Name":{
        "fathername": "Nagendrappa",
        "mothername": "Renuka",
    }
}

# print(student_data) 
# print(type(student_data))

# list= [('India','Delhi'),('UK','London')]

# dict1 = dict(list)

# print(dict1)

# out= student_data['Parents Name']

# out= student_data.get('School')           # key is not present here so get will give none not error

# out= student_data.keys()

# out= student_data.values()

# print(out)

# student_data['School'] =  "Assumption school"      #it wili add school as well to dictionary 

# student_data['Age'] = 18              # it will over write the age

student_data.update({'Age': 19})

print(student_data)

# states = ['Karnataka', 'Bihar', 'Maharastra', 'Tamilnadu']
# capital = ['Bengaluru', 'Patna', 'Mumbai', 'Chennai']

# print(dict(zip(states,capital)))ctionary.py