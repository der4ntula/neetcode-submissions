class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        # nums = [2,5,1,3]
        # target = 4
        # enumerateleyince: 0 2, 1 5, 2 1, 3 3
        
        # prevMap = {2: 0, 5: 1, 1: 2, 3: 3}
        # boylece prevMap[diff] diyerek index'e direkt
        # ulasabiliyoruz. eger index ve value'larin
        # yeri tam ters olsaydi bu value'ya correspondlayan
        # key nedir diyerek index'e ulasmak zor olurdu,
        # bir for loop daha gerektirirdi
    

        for i, v in enumerate(nums):
            diff = target - v # diff = 4 - 1 = 3
            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[v] = i
        

