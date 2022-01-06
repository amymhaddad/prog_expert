"""
https://www.programmingexpert.io/programming-fundamentals/assessment/3
"""

import operator

employees = [["John", 33, 65000], ["Sarah", 24, 75000], ["Josie", 29, 1000000], ["Jason", 26, 55000], ["Connor", 25, 110000]]
categories = {"name": 0, "age": 1, "salary": 2}



def v0_sort_employees(employees, sort_by):
print(v0_sort_employees(employees, "age"))
        


def sort_employees(employees, sort_by):
    index = categories[sort_by]

    return sorted(employees, key=operator.itemgetter(index))




def v2_sort(employees, sort_by):
    index = categories[sort_by]

    return sorted(employees, key=lambda x: x[index])



