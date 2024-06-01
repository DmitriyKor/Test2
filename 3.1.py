value1=int(input("Enter 1st figure \n"))
action=input("Enter action, +, -, * or / \n")
value2=int(input("Enter 2nd figure \n"))
if action=='+':
    result=value1+value2
elif action=='-':
    result=value1-value2
elif action=='*':
    result=value1*value2
elif action=='/':
    if value2!=0:
        result=value1/value2
    else:
        result=None
else:
    result=None
print("Result is ", result)
