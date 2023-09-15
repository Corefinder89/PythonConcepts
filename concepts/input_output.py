# input / output and string formatting
name=input("Please enter your name: ")
print(name)
integer1=int(input("Enter first number: "))
integer2=int(input("Enter second number: "))
sum = integer1+integer2
diff = integer1-integer2
print("The sum of two numbers is: " + str(sum))
print("The difference of two numbers is: " + str(diff))
print("The sum of two numbers is %d" % sum)
print("The difference of two numbers is %d" % diff)
print(f"The sum of the two numbers is {sum} and the difference of two numbers is {diff}")
# Placeholders in a formatted string
# %d -> integer
# %f -> float
# %s -> string
# %c -> character
print("The sum of the two numbers is %d and the difference of two numbers is %d" % (sum,diff))

name=input("Please enter your name: ")
age=int(input("Please enter your age: "))

print("My name is %s and my age is %d" % (name,age))

# Control statement in python
While loop
n = int(input("Enter n natural numbers:"))
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter = counter+1
print("The sum is", sum)

name = ["Soumyajit","Sathish","Chaitanya"]
search_name = input("Input name to search: ")

if search_name in name:
    print("%s is in the list" % search_name)
    pass
else:
    print("%s is not in the list" % search_name)

print("%s is in the list" % search_name) if search_name in name else print("%s is not in the list" % search_name)
# <control_statement> <condition> [if-else]
# pass if search_name in name else print("%s is not in the list" % search_name)
# Pass means not null operation, that means go to the next statement without any operation

for items in name:
    if search_name in items:
        print("name is present")
        break
    else:
        print("name not present")
        pass

n=5
sum=0
if n < 10: sum+=5;sum+=10
print(sum)

a=10
b=15
c=20

if a>b:
    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")
