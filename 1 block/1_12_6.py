# text for robot
kolichestvo = input()
n = int(kolichestvo[-2:])
stov = {5, 6, 7, 8, 9}
if n // 10 == 1 or n % 10 == 0 or n % 10 in stov:
     print (kolichestvo + " программистов")
elif n % 10 == 1:
     print (kolichestvo + " программист")
else:
     print (kolichestvo + " программиста")
