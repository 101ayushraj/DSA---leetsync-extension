class Solution:
    def findsol(self,x:float,n:int):
        if n==0:
            return 1
        elif n==1:
            return x

        if n%2==0:
            half=self.findsol(x,n/2)
            return half*half
        else:
            half=self.findsol(x,(n-1)/2)
            return x*half*half

    def myPow(self, x: float, n: int) -> float:
        divide=False
        if n<0:
            divide=True
            n=n*-1
        ans=self.findsol(x,n)
        if divide:
            ans=1/ans
        return ans