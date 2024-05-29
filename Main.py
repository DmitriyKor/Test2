x=input("Enter 4-digit figure")
print(type(x))
print("you entered:" + x)
x_int=int(x)
print(x_int // 1000)
print((x_int % 1000)//100)
print((x_int % 100)//10)
print((x_int % 10)//1)


x=input("Enter 5-digit figure")
print(type(x))
print("you entered:" + x)
x_int=int(x)
a1= x_int // 10000
a2= (x_int % 10000)//1000
a3= (x_int % 1000)//100
a4= (x_int % 100)//10
a5= (x_int % 10)//1
res=a5*10000 + a4*1000 +a3*100 + a2*10 + a1

print( res )
print (res )