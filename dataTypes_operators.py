# print("Hello python")
# userVar=input("Enter string:");y=50
# print(f"y={y}")
# print("y=",y)
# floatx=float(input("Enter the value:"))
# print(f"Float value is {floatx}")
# a=b=c=80
# print(f"a={a},b={b},c={c}")
# ax,bx,cx=50,20,3.5
# print(f"ax={ax}={bx},cx={cx}")

# #Task : peform arithmetic operations

# a,b=10,20
# print(f"Addition is {a+b},Substraction is {a-b},multiplication is {a*b},division is {a/b}")

# #list,Tuple,Set,Dictionary,Boolean

# int_var=10
# float_var=20.5
# string_var="hello"
# bool_var=True
# list_var=[44,55,"hello",88,66]
# list_var[0:]=2.5,3.5,7.5,5.5
# print(f"list = {list_var}");print(f"list index= {list_var[1]}")
# print(f"list = {list_var[:]}");print(f"list index= {list_var[1:4]}")
# print(f"list last index= {list_var[-1]}");print(f"list from last to second index= {list_var[-1:1:-1]}")
# set_var={44,22,77}
# list_var.append(7)
# list_var.extend([99,88,77,66])
# list_var.insert(2,7)
# print(f"list  = {list_var}")
# list_var.remove(77)
# list_var.pop(2)
# list_var.sort()
# list_var.reverse()
# print(f"list append ={list_var}")

# tuple_var=(11,77,22,44)
# print(f"tuple_var={tuple_var+(12,55)}")

# #set_var : accept only unique values 

# set_var={44,88,22}
# print(f"Type of set_var= {type(set_var)}")
# set_var.add(5)
# print(f"added value is:{set_var}")
# set_var.discard(88)
# print(f"discarded value is:{set_var}")
# union_set=set_var.union({44,22,66})
# print(f"union set is : {union_set}")
# set_difference=set_var.difference(union_set)
# print(f"set diff is:{set_difference}")

# #dictionary : key is mutable value can change

# dict_var={1:'A','B':2,'C':3}
# print(f"Dictionary ={dict_var}")
# dict_var['C']=3
# print(f"added value in Dictionary ={dict_var}")
# dict_var[1]=44
# print(f"updated value in Dictionary ={dict_var}")
# dict_var.pop('C')
# print(f"remove value in Dictionary ={dict_var}")
# keys=dict_var.keys()
# print(f"Dictionary ={keys}")
# values=dict_var.values()
# print(f"Dictionary ={values}")
# items=dict_var.items()
# print(f"Dictionary ={items}")

# #Arithmetic operators

# print(f"{a}+{b}={a+b}");print(f"{a}-{b}={a-b}")
# print(f"{a}*{b}={a*b}");print(f"{a}/{b}={a/b}")
# print(f"{a}%{b}={a%b}")

# #Comparison

# print(f"{a}=={b}:{a==b}");print(f"{a}!={b}:{a!=b}")
# print(f"{a}>{b}:{a>b}");print(f"{a}<{b}:{a<b}")
# print(f"{a}>={b}:{a>=b}");print(f"{a}<={b}:{a<=b}")

# #Logical

# t,f=True,False
# print(f"t and f:{t and f}");print(f"t or f:{t or f}")
# print(f"f not f:{not f}")

# #Bitwise operator

# m.n=5,3
# print(f"{m}&{n}:{m&n}");print(f"{m}|{n}:{m|n}")
# print(f"{m}^{n}:{m^n}")

#subnet mask
#network address range
#brodcast address
#classes

#Que 1 : user input ipv4 address lets convert this into binary and represent it in 8bit_value.8bit_value.8bit_value.8bit_value
# IPV4 in Decimal = 192.168.1.1
# IPV4 in binary = 11000000.10101000.00000001.00000001

#Que 2 : Satyam want to create network to connect 225 pc in single networks lets write program to help him 
# -take user input below 254 as number of pc in network and print IP address range,network address,broadcast address fro same
# Sample output:
# user Input number below 254 = 128 
# Host Range = 192.168.1.1 to 192.168.1.126
# network address : 192.168.1.0
# broadcast address : 192.168.1.127
# subnet mask: 255.255,255.128 i.e. /25

#modules

# import calendar as cal
# print("--------calendar program in python-----------")
# print("enter 'x' for exit")
# y=input("Enter year:")
# if y=='x':
#     exit()
# else:
#     m=input("Enter the month:")
#     yy=int(y)
#     mm=int(m)
#     print("/n",cal.month(yy,mm))

# #control statement
# #IF-ELSE-STATEMENT

# num=12
# if num>0:
#     print("number {num} is positive")
# elif num<0:
#     print("number {num} is negative")
# else:
#     print("number {num} is zero or not valid input")

# #FOR LOOP
# for i in range(1,5):
#     print(i)
# for i in range(5,1,-1):
#     print(i)

# #WHILE 
# count=1
# while count<5:
#     print(count)
#     count=count+1

# #BREAK
# for i in range(1,10):
#     if i==5:
#         print("Break Apply at",i)
#         break
#         print(f"loop iterate:{i}")

# #continue
# for i in range(1,10):
#     if i%2==0:
#         continue #skip even num
#     print(i)

# #pass
# for i in range(1,5):
#     pass

# #functions
# def greet():
#     print("hello")
# greet() #call fun
# def add(x,y):
#     greet()
#     return x+y
# res=add(5,2)
# print(f"result is : {res} ")


