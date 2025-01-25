class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        N = len(nums)
        arr = ["a" for _ in range(N + 1)]
        numMap = {}
        
        for n in nums:
            try:
                numMap[n] = numMap[n] + 1
            except:
                numMap[n] = 1

        for num in numMap.keys():
            if arr[numMap[num]] == "a":
                arr[numMap[num]] = [num]
            else:
                arr[numMap[num]].append(num)
        
        sol = []

        while N > 0 and k > 0:
            if arr[N] != "a":
                for x in arr[N]:
                    sol.append(x)
                    k -= 1
            N -= 1
        return sol


sol = Solution()
print(sol.topKFrequent(nums = [1], k = 1))


