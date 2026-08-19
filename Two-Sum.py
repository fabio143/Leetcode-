# Aug 13, 2026
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                soma = nums[i] + nums[j]
                if soma == target:
                    return [j, i]
# Não é a melhor solução, pois é O(n^2); a solução correta seria o uso de Hash Table.
