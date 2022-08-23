k, d = map(int, input().split())
nums = set(map(int, input().split()))
if nums == {0}:
    print(-1)
elif min(nums) == 0:
    if k > 2:
        nums.remove(0)
        a = str(min(nums))
        print(a + '0'*(k-2) + a)
    elif k <= 2:
        nums.remove(0)
        print(str(min(nums))*k)
elif min(nums) > 0:
    print(str(min(nums))*k)
else:
    print(-1)
