# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')

# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees )

# sort by name (Decending order)
employees.sort(reverse=True, key=get_name)
print(employees)

x = [3, 4, 5]
sorted(x, reverse = True)
#print(x)


people = {"Tim": 21, "Joe": 18, "Sarah": 25, "Jennie":26, "Bill":34}
ppl = sorted(people, key=people.get)
print(ppl)
#['Joe', 'Tim', 'Sarah', 'Jennie', 'Bill']

courses = {"math": 100, "art": 97}
c = sorted(courses)
print(c)
