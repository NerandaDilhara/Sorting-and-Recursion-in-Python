## 1st Discussed Code

def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1

        while (i > -1 and A[i] > key):
            A[i + 1] = A[i]
            i = i - 1

        A[i + 1] = key

def findRange(A):
    range = A[-1] - A[0]
    return range

def findMedian(A):
    if(len(A) % 2 == 0):
        median = (A[len(A) // 2] + A[(len(A) // 2) - 1]) / 2
    else:
        median = A[len(A) // 2]

    return median


A = []

for i in range(9):
    num = int(input("Mark: "))
    A.append(num)

print("Before Sorting: ", A)
insertionSort(A)
print("After Sorting: ", A) 

print("Range is: ", findRange(A))
print("Medain is: ", findMedian(A))


## 2nd Discussed Code

def func(num):
    if num == 1:
        return 1
    else:
        return num + (func(num-1))
    
while True:
    num = int(input("Enter number: "))

    if num == -1:
        break
    else:
        print("Output: ", func(num))

## 3rd Discussed Code

def func(num):
    if num == 1:
        return 1
    else:
        return (num-1) + (func(num-1))
    
while True:
    num = int(input("Enter number: "))

    if num == -1:
        break
    else:
        print("Output: ", func(num))





# A = [3, 56, 1, 30, 40, 5]

# A.sort()

# print(A)