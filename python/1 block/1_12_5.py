# from max to min to left

a = int(input())
b = int(input())
c = int(input())

list_numbers = (a, b, c)
x = max(list_numbers)
y = min(list_numbers)
z = (a + b+ c) - (x + y)
print(x)
print(y)
print(z)
