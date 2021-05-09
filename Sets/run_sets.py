def __main__():
    set_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    set_2 = {10, 20, 30, 50, 5, 80, 90, 100, 23, 4}

    union_result_set = set_1.union(set_2)
    print(union_result_set)

    intersection_result_set = set_1.intersection(set_2)
    print(intersection_result_set)

    difference_result_set = set_2.difference(set_1)
    print(difference_result_set)

    symmetric_difference_result_set = set_1.symmetric_difference(set_2)
    print(symmetric_difference_result_set)


__main__()
