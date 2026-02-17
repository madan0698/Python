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

# student_data= {
#     "Name": "Madan",
#     "Age": 27, 
#     "Skills": ["cricket","vollyball"],
#     "Parents Name":{
#         "fathername": "Nagendrappa",
#         "mothername": "Renuka",
#     }
# }

# print(student_data) 
# print(type(student_data))

# list= [('India','Delhi'),('UK','London')]

# dict1 = dict(list)

# print(dict1)

states = ['Karnataka', 'Bihar', 'Maharastra', 'Tamilnadu']
capital = ['Bengaluru', 'Patna', 'Mumbai', 'Chennai']

print(dict(zip(states,capital))) 