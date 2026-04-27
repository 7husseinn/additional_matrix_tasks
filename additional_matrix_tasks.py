#2
"""import random
def my_matrix(n,m):
    a=[]
    for i in range(n):
        a=a+[[0]*m]
        for j in range(m):
            a[i][j]=random.randint(-10,10)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    return a

def sutun_menfi(a):
    for j in range(len(a[0])):
        say=0
        cem=0
        for i in range(len(a)):
            if a[i][j]<0:
                say+=1
            cem+=a[i][j]
        if say>0:
            print(f"{j}-ci sutunda menfi sayi:",say)
        else:
            print(f"{j}-ci sutunun cemi:",cem)

n,m=map(int,input().split())
a=my_matrix(n,m)
sutun_menfi(a)"""


#3
"""import random
def my_matrix(n,m):
    a=[]
    for i in range(n):
        a=a+[[0]*m]
        for j in range(m):
            a[i][j]=random.randint(1,10)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    return a

def deyis(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]%2==1:
                a[i][j]=a[i][j]**2
            else:
                a[i][j]=a[i][j]//2
    return a

n,m=map(int,input().split())
a=my_matrix(n,m)
b=deyis(a)
print("Yeni matris:")
for i in b:
    for j in i:
        print(f"{j:4}",end="")
    print()"""


#4
"""import random
def my_matrix(n,m):
    a=[]
    for i in range(n):
        a=a+[[0]*m]
        for j in range(m):
            a[i][j]=random.randint(1,10)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    return a

def max_2x2(a):
    maks=0
    for i in range(len(a)-1):
        for j in range(len(a[0])-1):
            cem=a[i][j]+a[i][j+1]+a[i+1][j]+a[i+1][j+1]
            if cem>maks:
                maks=cem
    return maks

n,m=map(int,input().split())
a=my_matrix(n,m)
print("Maks 2x2 cemi:",max_2x2(a))"""


#5
"""import random
def my_matrix(n,m):
    a=[]
    for i in range(n):
        a=a+[[0]*m]
        for j in range(m):
            a[i][j]=random.randint(1,10)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    return a

def yeni_matris(a):
    b=[]
    for i in range(len(a)):
        b=b+[[0]*len(a[0])]
        for j in range(len(a[0])):
            cem=0
            if i>0:
                cem+=a[i-1][j]
            if i<len(a)-1:
                cem+=a[i+1][j]
            if j>0:
                cem+=a[i][j-1]
            if j<len(a[0])-1:
                cem+=a[i][j+1]
            b[i][j]=a[i][j]+cem
    return b

n,m=map(int,input().split())
a=my_matrix(n,m)
b=yeni_matris(a)
print("B matrisi:")
for i in b:
    for j in i:
        print(f"{j:4}",end="")
    print()"""


#7
"""import random
def my_matrix(n,m):
    a=[]
    for i in range(n):
        a=a+[[0]*m]
        for j in range(m):
            a[i][j]=random.randint(1,10)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    return a

def ziqzaq(a):
    netice=[]
    for i in range(len(a)):
        if i%2==0:
            for j in range(len(a[0])):
                netice+=[a[i][j]]
        else:
            for j in range(len(a[0])-1,-1,-1):
                netice+=[a[i][j]]
    return netice

n,m=map(int,input().split())
a=my_matrix(n,m)
print("Ziqzaq:",ziqzaq(a))"""

#11
"""import random
def my_matrix(n,m):
    a=[]
    for i in range(n):
        a=a+[[0]*m]
        for j in range(m):
            a[i][j]=random.randint(1,10)
    for i in a:
        for j in i:
            print(f"{j:4}",end="")
        print()
    return a

def simmetrik(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j]!=a[j][i]:
                return False
    return True

n=int(input())
m=n
a=my_matrix(n,m)
print("Simmetrikdir?",simmetrik(a))"""
