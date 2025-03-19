n1 = 1
n2 = 1
n3 = 2

user = int(input())

if user == 1:
    print(4)
    exit()

if user == 2:
    print(6)
    exit()


for i in range(4, user + 1):
    if i % 3 == 1:
        n1 = n2 + n3
    elif i % 3 == 2:
        n2 = n1 + n3
    else:
        n3 = n1 + n2

if user % 3 == 1:
    print(2*(n1 + n3 + n3 + n2))
    exit()
elif user % 3 == 2:
    print(2*(n2 + n1 + n1 + n3))
    exit()
else:
    print(2*(n3 + n2 + n2 + n1))
    exit()

