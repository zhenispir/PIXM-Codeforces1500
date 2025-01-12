a = input()
kishi = 0
ulken = 0
for i in range(len(a)):
    if a[i].islower() == True:
        kishi += 1
    else:
        ulken += 1

if ulken > kishi:
    print(a.upper())
else:
    print(a.lower())