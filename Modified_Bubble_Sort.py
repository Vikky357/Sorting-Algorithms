"""
@author: David
"""

#Modified Bubble Sort
size=int(input("Enter the size of array:"));
array=list(map(int,input("Enter the elements:").strip().split()))[:size]
print("Before Sorting:",array)
flag=1
arr=len(array)
while(arr and (flag==1)):
    flag=-1
    for j in range(0,len(array)-1):
        if(array[j]>array[j+1]):
            array[j],array[j+1]=array[j+1],array[j]
            flag=1
    arr-=1
print("After Sorting:",array)
