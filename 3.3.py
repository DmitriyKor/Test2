my_list = [12,16,56,6, 66, 78, 89, 67, 89]
print(my_list)
half_length=(len(my_list)+1)//2
my_new_list1=my_list[:half_length]
print(my_new_list1)
my_new_list2=my_list[half_length:]
print(my_new_list2)
my_result_list=[my_new_list1, my_new_list2]
print(my_result_list)
