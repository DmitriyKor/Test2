value=int(input("Введіть значення між 0 та 8640000\n"))

if not (0<value<8640000):
    Exit()

days,value=divmod(value, 24*60*60)
hours, value=divmod(value, 60*60)
minutes, value=divmod(value, 60)
seconds=value

res_str = str(days)
if (res_str[-1] in '567890') or ((days > 10) and (res_str[-2] in '1')):
    res_str = res_str+' днів'
elif res_str[-1] == '1':
    res_str = res_str + ' день'
else:
    res_str = res_str +' дні'

res_str=res_str+', '+str(hours).zfill(2)+':'+str(minutes).zfill(2)+':'+str(seconds).zfill(2)
print(res_str)
