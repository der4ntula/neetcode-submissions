class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Anagrams will have the exact same frequency of each word.

        # Here I match a hash map that is initially all-zero with 26 spots where each spot represents
        # a letter in the alphabet, and I iterate through each word in strs and nested in it I iterate through 
        # each letter of that word and I increment the reserved spot of the letters found in that word so that 
        # I end up with a map of letter-frequency for each word and I make that map a key in the alphabet2word dict 
        # and to its value I append each word that matches that map.

        alphabet2word = {}

        for word in strs:
            alphabet = [0] * 26
            for i in range(len(word)):
                alphabet[ord(word[i])-ord('a')] += 1
            alphabet = tuple(alphabet)
            if alphabet not in alphabet2word:
                alphabet2word[alphabet] = [word]
            else:
                alphabet2word[alphabet].append(word)

        return list(alphabet2word.values())
