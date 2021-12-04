# Minimum Number of Dining Rooms
# Given an array (list of meeting times), determine the minimum number of rooms needed to accomodate an arbitrary list of meeting times
# Return an integer representing the minimum number of rooms

# Clarifying questions:
# What format are the meeting times given in?
# Are the meeting times sorted? No
# Is it possible for end to be smaller than start? Overnight
# If one meeting ends at the same time another meeting starts, can they use the same room? Yes
# Are meetings constrained to one day? Yes
# Can I assume one time zone? Yes


# Example
# Input: [(1PM, 1:30PM), (1PM,2PM), (2PM, 3PM), (3PM,4PM)]
# Output: 2

from heapq import heappop, heappush
meetings = [[12, 16], [13, 13.5], [13, 14], [14, 15], [15, 16]]

# if list is empty, zero rooms
# non empty, at least 1 room
# sort by starting time
# using the first meeting time, assign numbers to start_time, end_time
# iterate to next meeting time, and determine if either start time or end time falls in the range of the first room
# 12 13 14 15 16 17 18 19
# ||||||||||||||
#     ||
#     |||
#       ||||
#          |||||


def min_rooms(meetings):
    meetings.sort()
    min_heap = []
