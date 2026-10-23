d = {}
print(type(d))

d1 = {
    "key":"sunny"
}

print(d1)

d2 = {
    "name":"sunny",
    "email":"email@gmail.com"
    }


print(d2)

d3 = {
    234:"sunny",
}

print(d3)


# d4 = {
#     234:"sunny",
#     @123:"not allowed any special key in place of key"
# }
# print(d4) #Gives Error

d4 = {
    234:"sunny",
    '@123':" allowed any special key in place of key if used using quotation"
}

print(d4) 


d5 = {
    234:"sunny",
    '_123':" allowed any special key in place of key if used using quotation",
    True:245665
}

print(d5) 

# Accessing value Now
print(d5[234])
print(d5[True])
print(d5[1]) #Get Boolena value Here True Beacuse 1 is Trur

d6={
    "name":"Ram",
    "mail_id":"sunny@gmail.com",
    "name":"sunny"
}
print(d6['name']) #Overwrite name here (Key should always we unique)

d7={
    "company":"abc",
    "courses":["webdev","ds","c++","js"]
}

print(d7["courses"])
print(d7["courses"][3])

d8={
    "number":[12,35,65,89,54,25],
    "assignment":(1,2,3,4,5,6),
    "launch_date":{'25 oct 2026','25 oct 2027'},
    "class_timing":{"wedev":"8am","dataScience":"10am","js":"11am"}
}

print(d8)
print(d8["launch_date"])





