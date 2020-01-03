
"""
@author: David
"""
#Insertion Sort
size=int(input("Enter the array size:"))
array=list(map(int,input("Enter the elements in array:").strip().split()))[:size]
print("Before sorting:",array)
for i in range(1,len(array)):
    val=array[i]
    ind=i
    while((array[ind-1]>val) and ind>=1):
        array[ind]=array[ind-1]
        ind-=1
    array[ind]=val
print("After Sorting:",array)      
