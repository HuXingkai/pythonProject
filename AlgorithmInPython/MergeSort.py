def merge(p,q,r,A):
    ##利用切片复制数组,和Java相比简单了很多
    left= A[p:q+1]
    left.append(999999)
    right=A[q+1:r+1]
    right.append(999999)

    #print(left,right)
    n1=0
    n2=0
    #遍历数组排序
    for i in range(p,r+1):
        if left[n1]<right[n2]:
            A[i]=left[n1]
            #print(A)
            n1+=1
        else:
            A[i]=right[n2]
            #print(A)
            n2+=1


def merge_sort(p,r,A):
    if p<r:
        q=int((p+r)/2)
        #print(p,q,r,A)
        merge_sort(p,q,A)
        merge_sort(q+1,r,A)
        merge(p,q,r,A)

A=[1,4,7,2,5,8,3,6,9]
merge_sort(0,len(A)-1,A)
print(A)
