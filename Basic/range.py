range(0,5)  # This is a generator function to generate integer (0,1,2,3,4) upper_bound - 1

print(list(range(5))) # To display Such data that's why we use list here
print(list(range(0,5,2))) # range(lower_bound,upper_bound,jump)
print(list(range(-10,0)))
print(list(range(-10,5)))



# ====================================================================================

l_11 = ["sudh","kumar","krish","naik"]


# for i in range(len(l_11)) :
#     print(l_11[i])


# print(range(len(l_11),0))
# print(list(range(0,len(l_11),1)))
# print(list(range(len(l_11))))
# print(list(range(len(l_11)-1)))
# print(list(range(len(l_11)-1,0,1))) #why it gives empty ?????
# print(list(range(len(l_11)-1,-1,-1)))
# for i in range(len(l_11)-1,-1,-1) :
#     print(l_11[i])




# ====================================================================================


l2 = [23,5,45,156,45,485,155,105,15,2,51,56,8,64,855,]

# print(len(l2))
# print(list(range(0,len(l2),2)))

# for i in range(0,len(l2),2) :
#         print(l2[i])

# l3 = [1,56,4,5,3,0]
# result =0
# for i in l3 :
#     # print(i)
#     result= result + i

# print(result)


# ====================================================================================

# t = (1,2,3,4,5)

# for i in t :
#     print(i)



# ====================================================================================

# t1 = {1,2,3,4,5}

# for i in t1 :
#     print(i)



# ====================================================================================

# s1 = "pwskills"

# for i in s1 :
#     print(i)

d = {
    "name":"radhe radhe",
    "class":"jsavascript",
    "topic":["basic","advancer","machjin leanrning"]
}

# for i in d.keys() :
#     print(d[i])


# for i in d.values() :
#     print(d[i])

for i in d.items() :
    print(i)