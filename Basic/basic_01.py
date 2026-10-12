
# 11
a = 21
print(type(a)); # Check Type of variable using type


# 222
b = True
c = False

d = b +c
print(d); # Sum of boolean value it treat behind the seen 0 and 1


# 33
v = 5+ 8j
print(v.real); # To Get Real Number
print(v.imag); # To get imaginary Number
print(v)


# 444  SCALING CONCEPT
s = "sunny raj"
print(type(s))
print(s[0]); # Forward Indexing
print(s[6]); # Forward Indexing
print(s[5]); # Forward Indexing
print(s[-1]); # Backward Indexing
print(s[-9]); # Backward Indexing
print(s[0:2]) # To Get starting and ending value When You use 2 the last value is not added It Gives data like LOWER BOUND TO UPPER BOUND - 1

#Get Alternate Date Now
print(s[0:9:2])
print(s[::2])
print(s[2::2])
# print(s[2::0]) # Gives error we cannot added 0 because slice step cannot be Zero
print(s[0:9:3])
print(s[0:9:1]) # Bydefault 1 if you not give any value


#To print in Reverse Order
print(s[::-1]) # I ADDED here only how much step you jump
name = "pwskills"
print(name[2:7:-1]) #" "

print(name[8:0])
print(name[8:0:-1])  

print(name[-2:8:1])
print(name[-2:-8:1])
print(name[-2:-8:-1])
print(name[-1:-8:-1])
print(name[-2::-1]) # If you not give upper bound then it access full data 
print(name[::-1]) # Bydeafult it take reverse indexing if you not provide upper & lower bound
print(name[:-8:-1])
print(name[::1])
print(name[:-90:]) # output blank
# print(name[90]) # string index of of raange
print(name[:-90:1]) # 
print(name[:-90:-1]) # 


# String Manipulation

c = 200
s1 = "This is my string class"
print(len(s1)) # To check length
print(s1.find('s')) # To Search any text Present OR not It Gives first value index of s not all
print(s1.find("my"))
print(s1.find("Is")) # If Value not exist it gives -1 Beaacuse it is a case sentitive language
print(s1.count('s')) # Count how many time s appear in this string
print(s1.count('st'))
print(s1.count('sti')) # If Not Exist the value you count that it give 0
print(s1.upper()) # To Convert Capital
print(s1.lower()) # To Convert Lower
print(s1.title()) # Set First letter capital of each words
print(s1.capitalize()) # It Set First letter only capital not each word capital letter

ss = "ral"
# print(ss+1) # Gives Error (Here i concatinate string to integer thats why it gives error)
print(ss + " good")


#Type Casting
aa = 1
print(ss+str(aa)) #Here I concatinate to convert integer to string
print(ss*3) # It Multiple 3 Times that value
# print(ss/4) # It Gives Error In Case Of String

# sentence = 'don't do copy and paste in my class'  (ERROR)
# sentence = `don't do copy and paste in my class`  (ERROR)
# If Single Quotes Used inside a string then you wrap that string with double quotes and vice-versa
sentence = "don't do copy and paste in my class" 
print(sentence)

# Multi Line Comment ========================================================= 11111
"""Example Here
I ,
Write
In THis 
Code , """


# Sinle Line Comment ========================================================= 2222

# I ,
# Write
# In THis 
# Code ,


