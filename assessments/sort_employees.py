"""
https://www.programmingexpert.io/programming-fundamentals/assessment/3
"""

import operator

employees = [["John", 33, 65000], ["Sarah", 24, 75000], ["Josie", 29, 1000000], ["Jason", 26, 55000], ["Connor", 25, 110000]]

def sort_employees(employees, sort_by):
    index = categories[sort_by]

    sortd_values = sorted(employees, key=operator.itemgetter(index))


    print(sortd_values)  


print(sort_employees(employees, "age"))




# people = [["john", 33, 65000]]
#
# for person in people:
#     if 33 in person:
#         print("here")
#
#
