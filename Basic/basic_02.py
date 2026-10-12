
#

l = [1,345,45,"sudh",True,(5+7j),345.56]
print(l)
print(type(l))
print(l[::2])
print(l[0])
# print(l[90]) #Gives Error Out Of Range Value You Provided
print(l[0:3])
print(l[-1])
print(l[::-1])
print(l[::2]) # Get Even Data
print(l[::3]) # Get Odd Data

s = "pwskills"
# print(l+s) #Error
print(list(s)+l)
print(l[3][0:2])
print(list(l[3])[0])
# print(l[4][0:2]) # This is not string so that why it gives error
print(str(l[4])[0:2])

# print(l+5) # Gives Error we cannot concatination list into integer

l1 = [3,4,5]
print(l+l1) # It Concatinate
# We Can Appened List TO List

print(l1*3) 
print(len(l)) # To Count Length
print(l.append(5))
print(l1.append(50))
# print(l.extend(4))
l.extend("sunny raj")
print(l)
l.extend([10,20,25])
print(l)
print(l1)
l1.insert(1,"tushar")
print(l1)
l1.insert(2,[10,30,50])
print(l1)
l1.insert(-1,"ram")
print(l1)
l1.insert(0,563)
print(l1)
l1.pop()
print(l1)
l1.pop(3) # Remove data according to indexes not to the value
print(l1)
l1.remove("ram") # It Remove first occurance of the value
print(l1)
l1.append([2,3,4])
print(l1)
# l1.remove(234) #This value is not in the list so thatwhy it gives error
print(str(l1[2])) # List is a mutable and String is a not muttable
l1.append(4)
print(l1.remove(4)) # If two data exist of same value, then remove first occurance value
print(l1)



l1[::-1] # It Reverse Temporaly
print(l1)

l1.reverse() #It reverese permanently
print(l1)
l2 = [9,5,15,9]
l2.sort() # Sort ascending to descending 
print(l2)
l3 = [34,"sudh",45,12,9,]
# l3.sort() # this is not work without inside that List it contain different type of data not same type of data

l4 = ["sudh","kumar","pwskills","data science"]
l4.sort()
print(l4)

# Descending order
l4.sort(reverse=True) #Sort according to descending order
print(l4)

print(l4.index("sudh")) #It Gives on which index this value exist
# print(l4.index("sudha")) If value not exist on the list then it gives error
print(l4.count("sudh")) # It Count how amny time this sudh repeat on that List
s = "sudh"
l5 = [3,4,5,6]
l5[0] = 30
print(l5) #Replace the value 

s = "audo"
print(s.replace('a','s')) #Not Replace Permanetly
print(s)
