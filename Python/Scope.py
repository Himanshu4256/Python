'''a=10
def print1(a):
    a= 11
    print("inside1:",a)
    x=globals() #function - eske baad jitne bhi var hai unhe ham function k andr acess update kr skte hai & update kr skte hai.
    a=15
    print("inside2:",a)
print1(a)
print("outside:",a)'''

'''def fab(n):
   a=0
   b=1

   if n==1:
       print(a)
   elif n<0:
       print("Wrong input")
   
   else:
       print(a)
       print(b)
       for i in range(2,n):
         c=a+b
         a=b
         b=c
         print(c)
fab(100)'''

# Squre root
'''def sq(a):
    return a*a
b=sq(5)
print(b)'''

#Squre root lambda function
f=lambda a:a*a
result=f(5)
print(result)

#Addition
f=lambda a,b:a+b
result=f(5,6)
print(result)

#Multiplications
x=lambda a:a*10
print("Mul=",x(20))
























