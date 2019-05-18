#在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
# #每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
# 判断数组中是否含有该整数
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for arr in array[:]:
            print(arr)
            if(self.search(0,len(arr)-1,target,arr)):
                return True
        return False
    def search(self,p,r,key,lists):
        if p<=r:
            q=int((p+r)/2)
            print(p,q,r)
            if lists[q]==key:
                return True
            elif lists[q]>key:
                return self.search(p, q - 1, key, lists)
            else:
                return self.search(q + 1, r, key, lists)
        return False

a=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(a)
print(Solution().Find(15,a))