#  252. Meeting Rooms

# Given an array of meeting time intervals where intervals[i] = [start_i, end_i], determine if a person could attend all meetings.


# Example 1
# ---------
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false

# Example 2
# ---------
# Input: intervals = [[7,10],[2,4]]
# Output:true


from typing import List


# Time complexity O(n log n)
# Space complexity O(n)


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        after_sort = sorted(intervals, key=lambda x: x[0])
        for i in range(len(after_sort) - 1):
            if after_sort[i][1] > after_sort[i + 1][0]:
                return False
        return True
