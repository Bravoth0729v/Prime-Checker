num =  int(input("Enter No: "))
Indic = False
num > 1
for i in range(2,num):
    if (num%i) == 0:
        Indic = True
    break
if Indic:
    print(num,"is not a Prime No")
else:
    print(num,"is a Prime No")
print("Thank You")