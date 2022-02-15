# put your python code here
a = int(input())
b = int(input())
count_kratnosti = 0
summ = 0
for i in range(a, b+1):
    if i % 3 == 0:
        count_kratnosti += 1
        summ += i
print(summ/count_kratnosti)