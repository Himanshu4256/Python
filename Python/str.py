                    #STRING METHODS

#txt1 = "python123"
#txt2 = "1234"
'''print(txt1.isalnum())
print(txt2.isalnum())
print(txt1.isalpha())
print(txt2.isalpha())
print(txt1.isdigit())
print(txt2.isdigit())
print(txt2.isnumeric())
print(txt2.isdecimal()) 
print('\u00b2'.isdecimal())
print('\u00b2'.isdigit())
print('\u00b2'.isnumeric())

print('\u2153'.isdecimal())
print('\u2153'.isdigit())
print('\u2153'.isnumeric())

#String find() & index() Methods
txt="Hello, Welcome"
print(txt.rfind("e"))
print(txt.rindex("e"))
print(txt.rfind("p"))
#print(txt.rindex("p"))
print(txt.find("e"))


str1 = "hello"
str2 = "True123"
print(len(str1))
print(len(str2))
print(len(True))
print("Length of string:",len(str1))'''

'''txt = " "
print(txt.isspace())
txt1 = 's'
x= print(txt1.isspace())

a = "Hello world@123"   # digits ko ignore krega like 123 string m ho to
b = "SRUGF HH hgf"
c = "Hi I Am Himanshu"
print(a.islower())
print(b.isupper())

print(b.istitle())
print(c.istitle())

# Lower() Method
print(a.lower())
print (b.lower())
print(a.upper())
print(b.title())
print(b.swapcase()) '''


  # max method
str1 = "aA"
str2 ="~01"
str3="python"
print(max(str1))
print(max(str2))
print(max(str3))
print(min(str3))


# center method()

'''line = "python is a programming language!!"
print(line.center(40))
print(line.center(40,'a'))'''

# ljust() method

'''txt = "hello"
print(txt)
print(txt.ljust(30),'is a programming language')
print(txt.ljust(20,'@'))
print(txt.rjust(30),'is a programming language')'''

# lstrip() Method
txt = "   banana "
txt1 = "banana     "
print(txt)
print(txt.lstrip()) # remove spaces in string
txt1=",,,,,ssaaww.....banana apple"
print(txt1.strip(",.asw")) # remove (,.asw)

print("--------------------------------------")

print(txt.rstrip()) # remove spaces in string
txt1=",,,,,ssaaww.....banana apple"
print(txt1.strip(",.asw"))


# Strip() Method -> dono trf se spaces remove kr dega (combination of lstrip & rstrip)


txt2 = "    jfdlsud fsd    "
print(txt2.strip())