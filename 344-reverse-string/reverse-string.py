class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def solve(s,left):
            if left >= len(s)-left:
                return s
            s[left],s[len(s)-1-left]=s[len(s)-1-left],s[left]
            solve(s,left+1)
        
        return solve(s,0)