"""
@author: David
"""
size=int(input("Enter the array elements:"))
array=list(map(int,input("Enter the elements of array:").strip().split()))
print("Before Sorting:",array)
l=len(array)
gap=l//2
while(gap):
    for i in range(gap,l):
        val=array[i]
        ind=i
        while((ind>=gap)and(array[ind-gap]>val)):
            array[ind]=array[ind-gap]
            ind-=gap
        array[ind]=val
    gap=gap//2
print("After sorting:",array)
