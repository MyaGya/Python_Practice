from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs:list):
        anagrams = defaultdict(list)
        for word in strs:
            anagrams["".join(sorted(word))].append(word)
        return anagrams.values()


S = Solution()
print(S.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

