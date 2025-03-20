temp_user = int(input())

temp = ""

for _ in range(temp_user):
    temp += " " + input()

mat = [int(i) for i in temp.split()]

li1 = []
li2 = []
while temp_user > 1:
    for h in range(int(temp_user/2)):
        for i in range(int(temp_user/2)):
            li1.append(mat[h*(temp_user)*2 + i*2])
            li1.append(mat[h*(temp_user)*2 + i*2 + 1])
            li1.append(mat[h*(temp_user)*2 + i*2 + temp_user])
            li1.append(mat[h*(temp_user)*2 + i*2 + temp_user + 1])
            li1.sort()
            li2.append(li1[2])
            li1 = []
    mat = li2
    li2 = []
    temp_user //= 2
    

print(mat[0])