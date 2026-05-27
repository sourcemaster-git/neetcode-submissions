class Solution:
    MAX_CHAR = 26
    def get_Hash(self, s):
        hashList = []
        freq = [0] * self.MAX_CHAR
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for i in range(self.MAX_CHAR):
            hashList.append(str(freq[i]))
            hashList.append("$")
        return ''.join(hashList)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mp = {}
        for i in range(len(strs)):
            key = self.get_Hash(strs[i])
            if key not in mp:
                mp[key] = len(res)
                res.append([])
            res[mp[key]].append(strs[i])
        return res
