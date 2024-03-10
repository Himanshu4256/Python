
#PEMDAS

'''i =1
while True:
    if i%3==0:
        break
    print(i)
    i+=1'''
list=[]
for i in range(5):
    name = input("Enter your name")
    list.append(name)
print(list)
def count(x):
    num=0

    for i in x:
        if len(i)>5:
            num=num+1
    print(num)
count(list)
