import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.
        :rtype: List of lists
        """
        # count dictionary
        res = collections.defaultdict(list)

        # go through each word and count intances of each letter
        for word in strs:
            count = [0] * 26  # num of letters

            for letter in word:
                count[ord(letter) - ord('a')] += 1

            # need to turn count list to tuple because list is mutable and tuple is not
            res[tuple(count)].append(word)

        return res.values()


sol = Solution()
sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# Time -> O(m * n) where m is the len of strs and n is average len of each word
# Space -> O(m) in the worst case
