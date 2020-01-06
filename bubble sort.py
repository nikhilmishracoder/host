n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
temp=0
j=0
c=0
# Write Your Code Here
for i in range(n):
    for j in range(0,n-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            print(a)  
            c=c+1
print("Array is sorted in %d"%c,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[n-1])
