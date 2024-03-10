'''L=[12,14,16,21,26]
for i in L:
    if i%5==0:
        print(i)
        break
else:
    print("not found")'''
n=7
for i in range(2,7):
    if(n%i==0):
        print("not prime")
        break
print("it's a prime")
