import numpy as np
arr = []
arr2 = []
m = int(input("enter row and column of first array :"))
n = int(input("enter row and column of second array :"))
Loop1 = m
Loop2 = n
while(Loop1/9 and Loop2/9 != 1):
    print("please enter again :blush:")
    Loop = int(input("Enter Your loop :"))
print("enter you array :blush:")
for i in range(Loop1):
    arr += [int(input(""))]
newarrm = np.asarray(arr)
newarrnumpy1 = newarrm.reshape(int(Loop1/3),3)
for j in range(Loop2):
    arr2 += [int(input(""))]
newarrm2 = np.asarray(arr2)
newarrnumpy2 = newarrm2.reshape(int(Loop2/3),3)
newarrnumpy = np.add(newarrnumpy1, newarrnumpy2)
print(newarrnumpy)