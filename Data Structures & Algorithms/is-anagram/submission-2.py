class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can get the length of the words in question
        # and run a for loop for that many times to add
        # letters and their corresponding counts for
        # each word in just one for loop

        # implementing .get(k, 0) makes code more fluent than
        # an if/else check

        # s = "racecar"
        # t = "carrace"

        # sMap = {r:2, a:2, c:2, e:1}
        # tMap = {c:2, a:2, r:2, e:1}

        if len(s) != len(t): # crucical step to avoid unnecessary iterations
            return False

        sMap, tMap = {}, {}

        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
        
        return sMap == tMap


        