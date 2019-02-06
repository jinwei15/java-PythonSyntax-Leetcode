# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#sol 1 pority queue

# Algorithm

# 1. Sort the given meetings by their start time.
# 2. Initialize a new min-heap and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.
# 3. For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
# 4. If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
# 5. If not, then we allocate a new room and add it to the heap.
# 6. After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.
import heapq
class Solution:
    def minMeetingRooms(self, intervals: 'List[Interval]') -> 'int':
        if len(intervals)==0: return 0
        intervals.sort(key = lambda x:x.start)
        # num_rooms = 1
        # for i in range(len(intervals)-1):
        #     if intervals[i].end > intervals[i+1].start:
        #         num_rooms += 1
        #iniatlise a min-heap to 
        heap = []
        heapq.heappush(heap, intervals[0].end)
        for i in intervals[1:]:
            if heap[0] <= i.start:
                heapq.heappop(heap)
            heapq.heappush(heap,i.end)
        return len(heap)
                
        
        
        
