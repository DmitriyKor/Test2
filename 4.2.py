my_list = [34, 0, 7, 9, 5, 0, 66, 8, 88, 99, 0, 3]
print(my_list)
list_len=len(my_list)
i=0
value_sum=0
while i<list_len:
    if (i % 2)==0:
        value_sum=value_sum+my_list[i]
    i=i+1
print(value_sum*my_list[list_len-1])
#method 2
print(sum(my_list[::2])*my_list[list_len-1])