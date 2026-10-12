t = (2,3,4,5,"sudh",45.56,False,45+457j,[3.4,5]) # Tuple uses parenthesis 
print(t)
print(type(t))
print(len(t))
print(t[3])
print(t[-3])
print(t[::-1])
# t[0] = 5 # Gives Error
print(t)
# Uses tuples in that place where we cannot modify that data in future
print(t.count(50))
print(t.index(False))


######################################################## 
# Set
s5 =  {}
print(type(s5))  # Gives Dictionary
s6 =  {2,3,4,55,6}
print(type(s6))  # Gives set
# s3 = {324,456,654,"sudgh",34.658,45+8j,[2,3,4]} # Gives Error because we cannot add tuple inside it set only contain immutable value not mutable

s3 = {324,456,654,"sudgh",34.658,45+8j}
s4 = {2,3,4,5,6,7,8,9,1,2,5,6,8,9,4,2,5,8,3,2,5}
print(s4) # Sets always gives unique value it remove duplicate value
s7 = {2,3,4,5,6,7,8,9,1,2,5,6,8,9,4,2,5,8,3,2,5,"Sudh","sudh"}
s8 = [2,3,4,5,6,7,8,9,1,2,5,6,8,9,4,2,5,8,3,2,5,"Sudh","sudh"]
print(s7)
print(set(s7)) 
print(list(set(s8))) # We can also used using this

s15 = {234,45,546,859,4587,"abc","efd",546,58,256}
print(s15) # set never arrange data in ascending to descending order
# print(s15[0]) # Gives Error
s15.add(4)
print(s15)
s15.remove("efd")
print(s15)
# s15.remove("esfd") # If not present in set then gives error
print(s15)

print(s15)

