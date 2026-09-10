eList = []
print(eList)
myList = [1, 2, 3, 4, "python"]
print(myList[1:4])      # Slicing the list

myList.append(5)
print(myList)

myList.insert(3,'a')        # (index, object)
print(myList)

add = 6, 7, 8
myList.extend(add)
print(myList)

myList.remove("python")     #Remove Elements by value
print(myList)

myList.pop(8)               # Remove Elements by Index
print(myList)

myList.clear()              #Remover all Elements
print(myList)
