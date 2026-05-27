class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = len(strs[0])
        res = []
        for s in strs:
            minLen = min(minLen, len(s))

        for i in range(minLen):
            ch = strs[0][i]

            for s in strs:
                if ch != s[i]:
                    return "".join(res)
            res.append(ch)
        return "".join(res)