'''line = "python is a programming language!!"
print(line.endswith('!!'))
print(line.endswith('language'))
print(line.endswith('language',0,32)) #32 last index hai'''

'''txt1 = "welcome to jungle"
print(txt1.split())
txt2 = "Hello, my name is Peter, I am 20 year old"
print (txt2.split())
txt3 = "apple#banana#cherry#orange"
print (txt3.split("#"))
txt4 = "apple#banana#cherry#orange"
#setting the maxsplit parameter to 1,will return a list with 2 elements!
print (txt4.split("#",1))'''

# splitlines() Methods

'''string = "welcome everyone to\rthe world of programming\n in python."
print(string.splitlines())
print(string.splitlines(0))
print(string.splitlines(True))'''

        #count() method
'''line = "python is a programming language!!"
sub = 'is'
print(line.count(sub))
print(line.count(sub,5,10))
print(line.count(sub,10,20))'''

# join() method
'''seq = ("a","b","c")
s="#"
print(s.join(seq))


my_dict={"rahul":"iphone","priyanka":"samsung","james":"realme"}
sep=" "
print(sep.join(my_dict))'''
#replace()
'''txt = 'i like bananas'
print(txt.replace("banana","apples"))
txt = "one two ka four four two ka one"
print(txt.replace("one","two"))'''

# capatalize()
'''line = "python is a programming language!!"
print(line)
print(line.capitalize())''' # string k 1st world ka 1st letter capital krna

#expandtabs()
'''txt = "H\te\t|\t|\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))'''

# zfill()
'''a="Hello"
b="welcome to the jungle"
c="10.000"
print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))'''

#encode()
txt = "My Name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

#decode()
'''str= "python is programming language"
str = str.encode('ascii','strict');
print("Encode String:",str)
print("Decode String:",str.decode('ascii','strict'))'''




     








