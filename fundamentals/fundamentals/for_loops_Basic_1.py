i = 0
sum = 0

for i in range(151):
    print(i)

for i in range(5, 1001, 5):
    print(i)

for i in range(1, 101):
    if(i%10 == 0):
        print("Coding")
    elif(i%5 == 0):
        print("Coding Dojo")
    else:
        print(i)

for i in range(0, 500000):
    if(i%2 == 1):
        sum += (i)
print(sum)

for i in range(2018, 0, -4):
    print(i)

for i in range(0, 101, 5):
    if i % 5 == 0:
        print(i)