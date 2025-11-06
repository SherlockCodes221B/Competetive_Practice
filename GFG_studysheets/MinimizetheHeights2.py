"""
Given an array arr[] denoting heights of n towers and a positive integer k.
For each tower, you must perform exactly one of the following operations exactly once.
Increase the height of the tower by k
Decrease the height of the tower by k
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower."""

class Solution:
    def getMinDiff(self, arr, k):
        arr.sort()  # Sorting the list
        n = len(arr)
        ans = arr[-1] - arr[0]  # Initial difference
        smallest = arr[0] + k
        largest = arr[-1] - k
        
        for i in range(n - 1):
            maxi = max(largest, arr[i] + k)
            mini = min(smallest, arr[i + 1] - k)

            if mini < 0:
                continue

            ans = min(ans, maxi - mini)

        return ans
