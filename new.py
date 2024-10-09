class Solution(object):
    def mySqrt(self, x):
        k=x
        for i in range(2,x+1):
            if i*i==x:
               return i
            elif x//i*i==i:
                  return x//i*i
              
solution = Solution()
a = int(input())  # Example input: '101' # Example input: '110'
result = solution.mySqrt(a)
print(result)