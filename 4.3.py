import random

my_list=[random.randint(0,100) for i in range(random.randint(3,10))]
print(my_list)
my_list2=[my_list[0], my_list[2], my_list[len(my_list)-2]]
print(my_list2)