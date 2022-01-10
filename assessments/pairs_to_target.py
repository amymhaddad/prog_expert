"""
https://www.programmingexpert.io/programming-fundamentals/assessment/5
"""


def pairs_sum_to_target(list1, list2, target):
    sums = []

    for i, v1 in enumerate(list1):
        for k, v2 in enumerate(list2):
            if v1 + v2 == target:
                sums.append([i, k])
    return sums
