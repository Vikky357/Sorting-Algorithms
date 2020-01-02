"""
@author: David
"""

#Bubble Sort
n=int(input("Enter the size of an array:"))
array=list(map(int,input("Enter the Elements:").strip().split()))[:n]
print("Before sorting:",array)
for i in range(len(array),0,-1):
    for j in range(0,len(array)-1):
        if(array[j]>array[j+1]):
            temp=array[j]
            array[j]=array[j+1]
            array[j+1]=temp
print("Sorted array:",array)
