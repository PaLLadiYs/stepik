# for i in 2, 3, 5:
#     print(i * i)
#
# for i in range(10):
#     print(i * i)
#
# for i in range(2, 5):
#     print(i * i)
# n = int(input())
#
# for i in range(n):
#     for j in range(n):
#         print('*', end='')
#     print()

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for row in range(c,d+1):
    print('\t', row, end='')
print()

for i in range(a, b+1):
    print(i,'\t',end='')
    for j in range(c, d+1):
        print(i * j, end='\t')
    print()