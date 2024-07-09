age = input("please enter your age ")
list1 = ["5","6","7","8","9","10","11","12"]
list2 = ["13","14","15","16","17","18"]

for i in range(len(age)):
    if i == list1:
        print("you are baby")
    elif i == list2: 
        print("you are an adult")