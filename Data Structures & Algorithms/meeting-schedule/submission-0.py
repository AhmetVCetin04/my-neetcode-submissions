"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        my_list = []

        for i, n in enumerate(intervals):
            my_list.append([n.start, i])
            my_list.append([n.end, i])

        my_list.sort(key= lambda time : time[0])

        for i in range(0, len(my_list), 2):
            if my_list[i][1] != my_list[i+1][1]:
                return False

        return True