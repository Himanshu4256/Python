'''import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
i=0
def rec():
    global i
    print("Hello",i)
    i=i+1
    rec()
rec()'''

'''def fab(n):
   a=0
   b=1

   if n==1:
       print(a)
   elif n<0:
       print("Wrong input")         #Wrong
   elif n>100:
       print("Your limit is crossed")
   
   else:
       print(a)
       print(b)
       for i in range(2,n):
         c=a+b
         a=b
         b=c
         print(c)
         fab(50)
fab(50)'''

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(5)
print(result)
