def fab(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n<0:
        print("Wrong input")
    elif n>100:
        print("Limit Crossed")
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fab(200)