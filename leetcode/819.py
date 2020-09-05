from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned
                 ]

        return Counter(words).most_common(1)[0][0]

s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))
