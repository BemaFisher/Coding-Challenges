#  347 - Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

import heapq
from typing import List
from collections import defaultdict


def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Solution using maxHeap. Using hashMap count instances of each num in nums then use maxHeap to find top k elements
    Time: O(klogn)
    Space: O(n) because of hashMap
    """
    count = defaultdict(int)

    for num in nums:
        count[num] += 1

    work = []

    for key, val in count.items():
        work.append((-val, key))

    heapq.heapify(work)

    output = []

    for i in range(k):
        item = heapq.heappop(work)
        output.append(item[1])

    return output


def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Bucket sort version
    - Make a hash table and count num of frequencies
    - Make an array where index == frequency and value at that index = value in the array
    - Loop through the above starting at the last index, if index.value is not empty, add to output array
    Time: O(n)
    Space: O(n) because of hashMap
    """

    freq_table = defaultdict(int)
    freq_arr = [[] for i in range(len(nums) + 1)]
    output_arr = []

    for num in nums:
        freq_table[num] += 1

    for key, val in freq_table.items():
        freq_arr[val].append(key)

    for i in range(len(freq_arr) - 1, 0, -1):
        for item in freq_arr[i]:
            output_arr.append(item)
            if len(output_arr) == k:
                return output_arr