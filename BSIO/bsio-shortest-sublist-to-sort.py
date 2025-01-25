nums = [1,2,3,4,3,2,1]

def l2r(nums):
    if len(nums) == 2:
        return 2 * int(nums[0] > nums[1])

    idx = 0
    sublistlens = []

    while idx <= len(nums) - 2:
        if nums[idx] > nums[idx + 1]:
            sublistlen = 0
            sublistlen += 1
            while nums[idx] >= nums[idx + 1] and idx <= len(nums) - 3:
                sublistlen += 1
                idx += 1
            sublistlens.append(sublistlen)
        idx += 1

    if len(sublistlens) == 0:
        return 0

    return min(sublistlens)

def r2l(nums):
    if len(nums) == 2:
        return 2 * int(nums[0] > nums[1])

    idx = 0
    sublistlens = []

    while idx >= len(nums) - 2:
        if nums[idx] > nums[idx + 1]:
            sublistlen = 0
            sublistlen += 1
            while nums[idx] >= nums[idx + 1] and idx >= len(nums) - 3:
                sublistlen += 1
                idx += 1
            sublistlens.append(sublistlen)
        idx += 1

    if len(sublistlens) == 0:
        return 0

    return min(sublistlens)

class Solution:
    def solve(self, nums):
        return sum([l2r(nums), r2l(nums)])



sol = Solution()
print(sol.solve(nums))
