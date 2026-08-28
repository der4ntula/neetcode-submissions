class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we should iterate through the word and record
        # how many times each letter appears into a hash map

        # if the two hash maps are equal to each other,
        # the words are anagrams of each other

        # s = "racecar"
        # t = "carrace"

        # sMap = {r:2, a:2, c:2, e:1}
        # tMap = {c:2, a:2, r:2, e:1}

        sMap = {}
        tMap = {}

        for letter in s:
            if letter not in sMap:
                sMap[letter]=1
            else:
                sMap[letter]+=1
        
        for letter in t:
            if letter not in tMap:
                tMap[letter]=1
            else:
                tMap[letter]+=1

        if sMap == tMap:
            return True
        else:
            return False