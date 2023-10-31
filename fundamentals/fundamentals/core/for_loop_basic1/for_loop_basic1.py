for i in range (0, 151):
    print(i)

for i in range (5,1001,5):
    print(i)

for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

sum = 0
for i in range(1,500001,2):
    sum += i 
print(sum)

low= 2
high= 9
mult= 3
for i in range(low,high +1):
    if i % 3==0:
        print(i)