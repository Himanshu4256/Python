unit = int(input("Enter Units :"))
if(unit<100):
    print("Your Bill is 0")
elif(unit>100 and unit<200):
    bill = (unit-100)*5
    print("Your Bill is",bill)
elif(unit>=200):
    bill = ((unit-100)*10)-500
    print("Your Bill is",bill) 
else:
    print("Pay Your Bill") 