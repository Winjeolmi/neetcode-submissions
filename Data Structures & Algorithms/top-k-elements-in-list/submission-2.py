class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int) # number : number of numbers

        for n in nums:
            hashmap[n] += 1
        
        sorted_hashmap = dict(sorted(hashmap.items(), key = lambda x: x[1], reverse = True))

        return list(sorted_hashmap)[:k]