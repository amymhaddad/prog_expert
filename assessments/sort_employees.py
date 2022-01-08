"""
https://www.programmingexpert.io/programming-fundamentals/assessment/3
"""

import operator

employees = [["John", 33, 65000], ["Sarah", 24, 75000], ["Josie", 29, 1000000], ["Jason", 26, 55000], ["Connor", 25, 110000]]
categories = {"name": 0, "age": 1, "salary": 2}

#Sol 1
def sort_employees(employees, sort_by):
    index = categories[sort_by]
    sorted_employees = []
    
    while len(employees) > 0:
        smallest_index = 0

        for i, employee in enumerate(employees):
            current_smallest_value = employees[smallest_index][index]

            if employee[index] < current_smallest_value:
                smallest_index = i
        
        next_employee = employees[smallest_index]
        sorted_employees.append(next_employee)
        employees.pop(smallest_index)
    return sorted_employees

#Sol 2
def sort_employees(employees, sort_by):
    index = categories[sort_by]
    return sorted(employees, key = lambda x: x[index])


#Sol 3
def sort_employees(employees, sort_by):
    index = categories[sort_by]

    return sorted(employees, key=operator.itemgetter(index))

#Sol 4
def sort(employees, sort_by):
    index = categories[sort_by]

    return sorted(employees, key=lambda x: x[index])