def binary_search(p,r,key,lists):
    if p<=r:
        q=int((p+r)/2)
        if lists[q]==key:
            return q+1
        elif lists[q]>key:
            return binary_search(p,q-1,key,lists)
        else:
            return binary_search(q+1,r,key,lists)
    return -1

def Find(target, array):
    # write code here
    len1=len(array)
    for arr in array[:]:
        return binary_search(0,len(arr),target,arr)

a=[[1,2],[3,4]]
print(Find(2,a))