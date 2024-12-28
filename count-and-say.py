class Solution:
    def countAndSay(self, n: int) -> str:
        def get_rle(s):
            stack = s[0]
            count = 1
            res = ""
            for x in s[1:]:
                # print("x:",x)
                # print("res:",res)
                if x==stack:
                    count+=1
                else:
                    res = res + str(count) + stack
                    stack=x
                    count=1

            res = res + str(count) + stack
            return res


        cur = "1"
        for i in range(1,n):
            cur = get_rle(cur)

        return cur