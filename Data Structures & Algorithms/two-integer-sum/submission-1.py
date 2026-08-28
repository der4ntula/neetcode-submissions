class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        # nums = [2,5,1,3]
        # target = 4
        # after enumeration: 0 2, 1 5, 2 1, 3 3
        
        # prevMap = {2: 0, 5: 1, 1: 2, 3: 3}
        # this way we can directly access the index using
        # prevMap[diff].

        # if the positions of index and values were reversed,
        # accessing the index by asking "what key corresponds to this
        # value" would be difficult and would require an additional 
        # for loop.
    

        for i, v in enumerate(nums):
            diff = target - v # diff = 4 - 3 = 1
            if diff in prevMap: # 1 is indeed a key in the hash map
                return [prevMap[diff], i]

            prevMap[v] = i