class Solution:
    def numDecodings(self, s: str) -> int:
        for i in range(len(s)):
            if s[i]=='0':
                if i==0:
                    return 0
                if s[i-1] not in ['1','2']:
                    return 0 
        
        def check(x,y):
            if 10 <= 10*x + y <=26:
                return True
            else:
                return False

        dp=[0]*(len(s) + 1)
        dp[0]=1
        dp[1]=1
        
        for i in range(2,len(s) +1):
            checked = check( int( s[i-2] ) , int (s[i-1] ))
            if s[i-1]=='0':
                dp[i]=dp[i-2]
                continue
            dp[i]=dp[i-1]+dp[i-2] if checked else dp[i-1]

        return dp[-1]
