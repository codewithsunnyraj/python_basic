# marks = 15
# marks = -15

# When we not convert it integer then by default input return string thats why we use int
marks = int(input("Enter Your Marks ")) 
# marks = float(input("Enter Your Marks ")) 

if marks >= 80:
    print("Greater than 80")
elif marks >= 60 and marks < 80 :
    print("Beyween 60 to 80")
elif marks >= 40 and marks < 60:
    print("Between 40 to 60")
else :
    print("Less than 40")



