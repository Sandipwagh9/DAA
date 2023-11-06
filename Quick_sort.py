def quickSort(arr):
    if(len(arr)<=1):
        return arr
    
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]

    return quickSort(left) + middle + quickSort(right)

arr=[98,45,46,67,95,34 ,34]

ans=quickSort(arr)
print(ans)
