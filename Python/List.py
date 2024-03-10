#UPDATION LIST
'''list=['physics','chemistry',1997,2000]
print(list)
print(len(list))
del list[2]
print("after deleting",list)'''

#Example of len() function
'''list1=["physics",'che','math']
print(len(list1))'''

'''#xample of max() function
list1=[1,2,3,4]
print("max value ele", max(list1))


#example of min() function
print("min is ",min(list1))

#example of list() function (typecasting)
atuple = (123,'c++','java','python')
list1=list(atuple)
print("list element:",list1)
str="Helloo world"
list2=list(str)
print("list element:",list2)'''

               #Methods
list1 =['c','java','python','c']
list1.append('c#')
print("updated list",list1)
print("count list is",list1.count('c'))
list2=[1,2,3,4]
list1.extend(list2)
print("Extended list",list1)
print('java index is ',list1.index('java'))
#print('index of java is',list1.index('shap'))
list1.insert(3,'c++')
print('Final List',list1)

list1.pop(2)
print("pop list Now",list1)
#list1.remove('python')
#print("after remove",list1)

list1.reverse()
print(list1)

#list1.sort()  #ssort k liye all data type same hone chahiye
#print(list1)
list2=list1.copy()
print(list2)


