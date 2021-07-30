Num = int(input('Enter your loops:'))
Numtotal = []
for i in range(Num) :
    data = int(input('Enter your Data:'))
    Numtotal += [data]
Numtotal.sort()
m= Numtotal[0]
print('Minimum Number is:', m)
M= Numtotal[Num-1]
print('Maximum Number is', M)