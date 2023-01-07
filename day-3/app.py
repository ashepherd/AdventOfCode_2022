import json
import string

"""
https://adventofcode.com/2022/day/3
"""

PRIORITY_LIST = string.ascii_lowercase + string.ascii_uppercase

def get_priority(type):
    return PRIORITY_LIST.index(type) + 1

def find_common_item_type(one, two):

    return ''.join(set(one).intersection(two))

class Item:
    def __init__(self, type):
        self.type = type
        self.priority = get_priority(type)

class RuckSack:
    def __init__(self, contents):
        self.contents = ''.join(filter(str.isalnum, contents))

        one, two = self.split_contents()
        self.common_item_type = Item(find_common_item_type(one, two))

    def split_contents(self):
        return (self.contents[:len(self.contents)//2], self.contents[len(self.contents)//2:])

class Group:
    def __init__(self):
        self.sacks = []

    def add_sack(self, sack):
        self.sacks.append(sack)

    def find_badge(self):
        common_1_2 = find_common_item_type(self.sacks[0].contents, self.sacks[1].contents)
        return find_common_item_type(common_1_2, self.sacks[2].contents)
        

file = open('input', 'r')
lines = file.readlines()

answer_pt1 = 0
answer_pt2 = 0
group = Group()
bag = 0
for line in lines:
    sack = RuckSack(line)
    answer_pt1 += sack.common_item_type.priority

    group.add_sack(sack)
    bag += 1

    if bag % 3 == 0:
        badge = group.find_badge()
        priority2 = get_priority(badge)
        answer_pt2 += get_priority(badge)
        group = Group()



print("Answer for part1: {ans}".format(ans=answer_pt1))
print("Answer for part2: {ans}".format(ans=answer_pt2))

