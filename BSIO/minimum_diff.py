class Solution:
    def solve(self, a, b):

        a = set(a)
        b = set(b)

        if len(set.intersection(a, b)) > 0:
            return 0

        a = list(a)
        b = list(b)

        a.sort()
        b.sort()
        blist = b
        a = a[::-1]
        difflist = []

        for b in blist:
            r = len(a)-1
            l = 0
            m = (l + r) // 2
            diff = abs(a[m] - b)

            while l <= r:

                ldiff = abs(a[l] - b)
                rdiff = abs(a[r] - b)

                if ldiff < diff:
                    r = m - 1
                    m = (l + r) // 2
                    diff = abs(a[m] - b)
                elif rdiff < diff:
                    l = m + 1
                    m = (l + r) // 2
                    diff = abs(a[m] - b)
                else:
                    break
            difflist.append(abs(a[m] - b))

        return(min(difflist))


lst0 = [1, 1, 2]
lst1 = [0]
solver = Solution()
print(solver.solve(lst0, lst1))
