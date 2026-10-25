# a = 1

# while a <= 10 : # First it check condition then execute in for loop condition is not checked
    # print(a)
    # a = a + 1


# ==================================================================================== sum of the number till sum point

# n = int(input("Enter Your Limit "))
# starting_point = 0
# counter = 1

# while counter <= n :
#     starting_point = starting_point + counter
#     counter = counter + 1
# print(starting_point)
      

# ==================================================================================== Factorial




# ==================================================================================== Fibnonacci series

# number = int(input("Enter the nUmber of element you are lookingt for "))

# a,b = 0,1
# counter = 0
# while counter < number :
#     print(a)
#     c = a+b
#     a = b
#     b = c
#     counter = counter + 1


# ==================================================================================== Reverse String

# s = "sudh"
# word = input("Enter the a string ")

# print(len(s))
# reverse = ""
# length = len(s)
# while length > 0 :
#     reverse = reverse + word[length - 1]
#     length = length - 1
# print(reverse)


# ==================================================================================== Print Table Of Number 

# table = int(input("Enter Table Of "))
# starting = 1
# while starting <= 10 :
#     print(table, "* ",starting, "= ", table * starting)
#     starting =  starting + 1


 
# ==================================================================================== Using Else in while

# n = 5
# i = 1
# while i < n :
#     print(i)
#     i = i + 1
# else :
#     print("This will be executed one your while will completed it successfully")


n =5
i = 1
while i < n :
    print(i)
    if i == 3 :
        break
    i = i + 1
else :
    print("This will be executed one your while will completed it successfully")