List= [10,20,30]

#methods in list
#1.append()

List.append(40)
print(List)

#2.Extend()

List.extend([40,50])
print(List)

#3.insert()

List.insert(3,60) #(index,x)
print(List)

#4.pop()

List.pop(4)
print(List)

#5.pop()

List.pop() # by default it will remove the  last element of the list
print(List)

#6.remove()

List.remove(60)
print(List)

#7.sort

List.sort()
print(List)

#8.reverse

List.reverse()
print(List)

#9.clear

List.clear()
print(List)

#10.copy

new_list=List.copy
print(new_list)