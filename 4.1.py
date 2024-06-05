my_list = [34, 0, 7, 9, 5, 0, 66, 8, 88, 99, 0, 1]
print(my_list)
list_len=len(my_list)
i=0
while i<list_len:
    if my_list[i]==0:
        my_list.pop(i)
        my_list.insert(list_len, 0)
    i=i+1
print(my_list)
