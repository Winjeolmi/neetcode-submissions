class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_of_nums = defaultdict(int) # number : number of numbers
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            num_of_nums[n] += 1
        
        for n, c in num_of_nums.items():
            freq[c].append(n)
        
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result