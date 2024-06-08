import string
import keyword

var_name=input("Enter name of variable\n")
if len(var_name)==0:
    exit()
if not var_name.islower():
    exit()
if ' ' in var_name:
    exit()
for char in string.punctuation:
    if (char!='_') and (char in var_name):
        exit()
if var_name in keyword.kwlist:
    exit()
if '__' in var_name:
    exit()

print('variable is good')



