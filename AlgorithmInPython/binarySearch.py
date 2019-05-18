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

A=[1,2,3,4,5,6,7,8,9]
num=int(input("请输入值\n>"))
print(binary_search(0,len(A)-1,num,A))
