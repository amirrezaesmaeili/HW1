n = int(input("Enter the desired number of laptops : "))

L = []
for i in range(0, n):
    s = input("Enter the price and quality of the laptop : ").split(",")
    L.append(s)
for i in range(0, len(L)):
    for j in range(0, 2):
        L[i][j] = int(L[i][j])

flag = 0

for i in L:
    for j in range(1, len(L)):
        if ((i[1] >= L[j][1]) and (i[0] < L[j][0])):
            flag = 1

if flag == 1:
    print("found")
else:
    print("not found")
