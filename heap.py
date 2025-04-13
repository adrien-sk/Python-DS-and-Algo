# Return the K most frequent elements in NUMS

# V1 : Fill the heap storing -count (cause default heap is MIN heap), then heap pop for K times
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    res = []
    heap = []
    hmap = defaultdict(int)

    for num in nums:
        hmap[num] += 1
    
    for num, count in hmap.items():
        heapq.heappush(heap, (-count, num))

    for i in range(k):
        count, num = heapq.heappop(heap)
        res.append(num)

    return res



# V2 : While we fill the heap, everytime we heap push, check if we have more item than K. If so, heap pop the minimum value
# At the end, we have the 3 bigger values

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    res = []
    heap = []
    hmap = defaultdict(int)

    for num in nums:
        hmap[num] += 1

    for num, count in hmap.items():
        heapq.heappush(heap, (count, num))

        if len(heap) > k:
            heapq.heappop(heap)

    for count, num in heap:
        res.append(num)
    
    return res