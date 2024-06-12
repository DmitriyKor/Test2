import string
range_str=input("Enter range _-_\n")
ind1=string.ascii_letters.index(range_str[0])
ind2=string.ascii_letters.index(range_str[2])
if ind2<ind1:
    ind1, ind2=ind2, ind1
res_str=string.ascii_letters[ind1:ind2+1]
print(res_str)