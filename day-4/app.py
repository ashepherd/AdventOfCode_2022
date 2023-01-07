import json
import string

"""
https://adventofcode.com/2022/day/4
"""



class Pairing:
    def __init__(self, assignment):
        self.assignment = assignment
        self.groupings = assignment.split(',')
        one = self.groupings[0].split('-')
        two = self.groupings[1].split('-')
        one_min = int(one[0])
        one_max = int(one[1])
        two_min = int(two[0])
        two_max = int(two[1])
        self.within, self.container = self.is_within(one_min, one_max, two_min, two_max)
        self.unique = self.is_unique(one_min, one_max, two_min, two_max)

    def is_within(self, one_min, one_max, two_min, two_max):
        
        one_contains = one_min <= two_min and one_max >= two_max 
        two_contains = two_min <= one_min and two_max >= one_max
        if (one_contains is True):
            return True, '1'
        elif two_contains is True:
            return True, '2'
        return False, None

    def is_unique(self, one_min, one_max, two_min, two_max):
        return one_min > two_max and one_min > two_min or one_max < two_min and one_max < two_max


        

file = open('input', 'r')
lines = file.readlines()

answer_pt1 = 0
answer_pt2 = 0

for line in lines:
    pair = Pairing(line.strip())
    if pair.within is True:
        answer_pt1 += 1
    if pair.unique is False:
        answer_pt2 += 1

print("Answer for part1: {ans}".format(ans=answer_pt1))
print("Answer for part2: {ans}".format(ans=answer_pt2))

