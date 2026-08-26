n = 8
letters ="abcdefgh"
for i in range(n):
    print(8-i,end="  ")
    for j in range(n):
        print("*",end="  ")
    print()
print("   ",end="")
for j in range(n):
    print(letters[j],end="  ")