def common_elements():
    set1 = set([item for item in range(0, 100, 3)])
    set2 = set([item for item in range(0, 100, 5)])
    return(set1.intersection(set2))



assert common_elements() == {0, 75, 45, 15, 90, 60, 30}