import json
import string

"""
https://adventofcode.com/2022/day/5
"""

def parse_crate_line(line):
    return [i for i, ltr in enumerate(line) if ltr == '[']

class Ship:
    def __init__(self):
        self.rows = {}
        self.order = []

    def get_top_crates(self):
        print(self.rows)
        str = ''
        print(self.order)
        for r in self.order:
            print(r, self.rows[r])
            str += self.rows[r][-1]
        return str

    def place_crates(self, line, positions):
        for p in positions:
            row_num = str(p//4 + 1)
            if row_num not in self.rows:
                self.rows[row_num] = []
            self.rows[row_num].append(line[p+1])

    def reverse_rows(self):
        for r in self.rows:
            self.rows[r].reverse()

    def label_rows(self, labels):
        while("" in labels):
            labels.remove("")
        self.order = labels

    def cratemover_9000(self, line):
        directions = line.split(' ')
        num_of_crates = int(directions[1])
        print('From:', self.rows[directions[3]])
        print('To:', self.rows[directions[5]])
        print('# of crates:', num_of_crates)

        for x in range(0,num_of_crates):
            self.rows[directions[5]].append( self.rows[directions[3]].pop())

        print('From:', self.rows[directions[3]])
        print('To:', self.rows[directions[5]])

    def cratemover_9001(self, line):
        directions = line.split(' ')
        num_of_crates = int(directions[1])
        print('From:', self.rows[directions[3]])
        print('To:', self.rows[directions[5]])
        print('# of crates:', num_of_crates)

        move = []
        for x in range(0,num_of_crates):
            move.insert(0, self.rows[directions[3]].pop())
        self.rows[directions[5]].extend(move)

        print('From:', self.rows[directions[3]])
        print('To:', self.rows[directions[5]])

file = open('input', 'r')
lines = file.readlines()
has_crates = False
has_rows = False
ship = Ship()
for line in lines:
    prepped_line = line.replace("\n", "")

    if '' == prepped_line.strip():
        continue

    if False == has_crates:
        positions = parse_crate_line(prepped_line)
        if not positions:
            ship.reverse_rows()
            print(ship.rows)
            has_crates = True
        else:
            ship.place_crates(prepped_line, positions)    
            continue

    if False == has_rows:
        row_ids = prepped_line.split(' ')
        ship.label_rows(row_ids)
        has_rows = True
        continue

    # part 1
    #ship.cratemover_9001(prepped_line)
    # part 2
    ship.cratemover_9001(prepped_line)

print("Top Crates:", ship.get_top_crates())