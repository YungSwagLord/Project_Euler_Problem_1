# Input maximum range of "x"
x = input("Enter your maximum range: ")
print(x)
# Input multiple of "y"
y = input("Enter your first multiple: ")
print(y)
# Input multiple of "z"
z = input("Enter your second multiple: ")
print(z)

array = []   
i = 1
#array.append(i)
#def apply_func(L,x):
#List all the natural numbers below "x" that are multiples of "y" or "z"
for i in range(int(x)):
    if i % int(y) == 0:
        array.append(i)
    elif i % int(z) == 0:
        array.append(i)


print(f"These are the multiples: {array}")
print(f"This is the sum of the multiples {sum(array)}")







# find the sum of all the multiples of "z" or "y" below "x"
#Sum(list)



