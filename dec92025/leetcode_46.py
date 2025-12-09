class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        sol , res =[], []

        def backtrack():
            if len(sol)==len(nums):
                res.append(sol[:])
                return
            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()

        backtrack()
        return res


        
#recusrive backtracking solution