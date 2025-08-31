num = float(input("enter the number:"))
if num > 0:
    print("positive number")

#add an else block to handle both cases
num =float(input("enter a number"))
if num > 0:
    print("positive")
else:
    print ("negative")

#creats multiple conditions using elif./if with logical and

num = float(input("emter a number:"))
if num > 0:
    print("positive")
elif num == 0:
    print("zero")
else:
    print("negative")

#putting one if inside another/ nested if statementes/if with logical or
age=int(input("enter age"))
if age >=10:
    if age < 22:
        print("young adult")

#scan multiple numbers together
numbers = list(map(float,input("enter numbers: ").split()))
#check each numbers
for num in numbers:
    if num > 0:
        print(num,"is positive")
    elif num == 0:
        print(num ,"is zero")
    else:
        print(num, "is negative")

numbers = list(map(float,input("enter numbers: ").split()))
#check each numbers
result = []
for num in numbers:
    if num > 0:
        result.append("positive")
    elif num == 0:
        result.append("zero")
    else:
        result.append("negative")
print("numbers:",numbers)
print("result:",result)