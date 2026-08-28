class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dict use in Python causes overhead,
        # so instead we can make use of the fact
        # there are 26 letters in the English alphabet
        # and implement a hash table

        # we can initiate each letter's spot as 0,
        # and if letter exists in first word the letter's
        # spot will be incremented by 1 and if letter exists
        # in second word as well the letter's spot will be
        # decremented by 1

        # if, at the end, all spots are zero, the words are
        # each other's anagrams

        # s = "racecar"
        # t = "carrace"

        if len(s) != len(t): # crucical step to avoid unnecessary iterations
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i])-ord('a')]+=1
            count[ord(t[i])-ord('a')]-=1
        
        return count == [0] * 26

        