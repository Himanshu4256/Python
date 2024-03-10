'''n = int(input("enter your candies"))
i=1
while(i<=n):
    print("candy")
    i=i+1'''
av=5
n=int(input("enter candy"))
i=1
while i<=n:
    if i>5:
        print("Sorry! out of stock")
        break
    print("candy")
    i=i+1
print("Finish")
