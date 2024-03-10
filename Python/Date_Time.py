#import datetime
#print(dir(datetime))
import datetime
'''a = datetime.date(2202,8,4)
print(a)
print(type(a))'''
date_object = datetime.date.today()
print(date_object)


'''from datetime import date
ts = date.fromtimestamp(12349497) #ye seconds hai & eski starting 01-jan-1970 se hoti hai
print("Date=",ts)'''

from datetime import time
'''a = time()
print("a =", a)
b=time(8,52,42)
print("b =",b)
c=time(hour = 9, minute = 32, second = 22)
print("c =",c)
d= time(10,43,32,234566)
print("d =",d)'''

'''a = time(10,45,46)
print("hour =",a.hour)
print("hour =",a.minute)
print("hour =",a.second)'''
#from datetime import datetime(consist in python)

import datetime
a = datetime.datetime.now()
print(a)


from datetime import datetime,date
t1 = date(year=2018,month=7,day=12)
t2 = date(year=2017,month=12,day=23)
t3=t1-t2
print("t3=",t3)
t4=datetime(year=2018,month=7,day=12,hour=7,minute=9,second=33)
t5=datetime(year=2019,month=6,day=10,hour=5,minute=55,second=13)
t6=t4-t5
print("t6=",t6)
print("Type of t3",type(t3))
print("Type of t4",type(t4))

print("-----------------------------------------------------------")

from datetime import timedelta
t = timedelta(days=5,hours=1,seconds=33,microseconds=233423)
print("total seconds =",t.total_seconds())  




