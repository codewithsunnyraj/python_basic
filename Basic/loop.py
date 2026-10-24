l = [1,2,3,4,5,6,7,8,9]

# for i in l :
#     print(i)


# =========================================================================================================================================================

# for i in l :
#     print(i+1)


# =========================================================================================================================================================

# l1 = []

# for i in l :
#     l1.append(i+1)

# print(l1)


# ======================================================================================================================================================

# l2 = ["sudh","kumar","pwskills","course"]
# l3 = []
# for i in l2 :
#     # print(i.upper())
#     print(l3.append(i.upper()))



# ======================================================================================================================================================

# l2 = ["sudh","kumar","pwskills","course",1,2,3,56,85,56.36,"abc"]
# l3_int = []
# l4_str = []
# for i in l2 :
#    if type(i) == int or type(i) == float :
#       l3_int.append(i)
#    else :
#       l4_str.append(i)

# print(l3_int)
# print(l4_str)


# ======================================================================================================================================================

# s1 = [1,2,3,4,5]

# for i in s1 :
#    print(i)
#    print(type(i))


# ====================================================================================

l_11 = ["sudh","kumar","krish","naik"]

# for i in l_11 :
#     print(i)
# else :  # When for loop is executed after that else run if he break in between then not print else block
#     print("If For loop is able to complete itself then only else will execute")



# for i in l_11 :
#     if i == 'kumar' :
#         break
#     print(i)




# for i in l_11 :
#     if i == 'kumar' :
#         break
#     print(i)
# else :
#     print("Execute this if for loop is able to complete itself")


for i in l_11 :
    if i == 'kumar' :
        continue
    print(i)
else :
    print("If Executed for loop after that it print")