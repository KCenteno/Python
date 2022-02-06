#        1 Update Values in Dictionaries and Lists


# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15
# print(x)
# students[0]['last_name'] = 'Bryan'
# print(students)
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)
# z[0]['y'] = 30
# print(z)

#          Iterate Through a List of Dictionaries


# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(students):
#     x = ""
#     for i in range(len(students)):
#         x += (students[i]['first_name'])
#         x += (students[i]['last_name'])
#         x += (" - ")
#     return x

# print(iterateDictionary(students))


#      Get Values From a List of Dictionaries


def iterateDictionary(students):
    x = ""
    for i in range(len(students)):
        x += (students[i]['first_name'])
    return x

print(iterateDictionary(students))


def iterateDictionary(students):
    x = ""
    for i in range(len(students)):
        x += (students[i]['last_name'])
    return x

print(iterateDictionary(students))


#       Iterate Through a Dictionary with List Values


# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(dojo):
#     print(str(len(dojo['locations'])) +' locations')
#     for i in range(len(dojo['locations'])):
#         print(dojo['locations'][i])
#     print(str(len(dojo['instructors'])) +' instructors')
#     for j in range(len(dojo['instructors'])):
#         print(dojo['instructors'][j])

# print(printInfo(dojo))