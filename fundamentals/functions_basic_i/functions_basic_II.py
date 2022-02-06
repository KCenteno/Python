# Countdown

def countdown(Num):
    c = []
    for i in range(Num, -1, -1):
        c.append(i)
    return c
print(countdown(5))


# Print and Return

def PnR(a,b):
    print (a)
    return b
print(PnR(3,6))


# First Plus Length

def FpL(list):
    return list[0] + len(list)
print(FpL([5,4,8,7,2]))


# Values Greater than Second

def VtS(arr):
    l = []
    b = 0
    if(len(arr) < 2):
        return False
    for i in range(0, len(arr)):
        if(arr[i] > arr[1]):
            l.append(arr[i])
            b = b+1
    print(b)
    return l
print(VtS([5,2,3,2,1,4]))
print(VtS([5]))


# This Length, That Value

def TlTv(a, b):
    l = []
    for i in range(0, a):
        l.append(b)
    return l

print(TlTv(3,6))