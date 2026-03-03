# file1 = open('file1.txt', 'w')
# file1 = open('file1.txt', 'a+')

# file1.seek(0)

# print(file1.readline())
# print(file1.readline())

# for line in (file1.readlines()):
#     print(line)

# file1 = open('file1.txt', 'r')
# file1.close()

with open('ok/file1.txt', 'r') as f2:
    print(file1.read().lower().count('in'))
