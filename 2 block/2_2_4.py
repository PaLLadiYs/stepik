i = 1
while True:
    i = int(input())
    if i < 10:
        continue
    if i > 100:
        break
    else:
        print(i)