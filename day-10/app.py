import sys

INPUT = 'input'

class CPU:
    def __init__(self):
        self.X = 1
        self.cycles = [1]

    def signal_strength(self, cycle):
        i = cycle - 1
        return self.cycles[i] * cycle

    def past_cycles(self, num):
        past_cycle_fix = -2
        neg_num = -1 * num
        past = []
        num_cycles = len(self.cycles)
        while neg_num < 0:
            past.append((num_cycles + 1 + neg_num + past_cycle_fix, self.cycles[neg_num]))
            neg_num += 1
        return past

    def addx(self, value):
        cost = 2 #cycles
        self.cycles.append(self.X)
        self.X += value        
        self.cycles.append(self.X)
    def noop(self):
        cost = 1 #cycle
        self.cycles.append(self.X)


class CRT:
    def __init__(self):
        self.screen = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
        }
        self.row = 0

    def draw(self, register):
        for idx,val in enumerate(register):
            sprite = (val-1,val,val+1)
            s = '#' if idx in sprite else '.'
            self.screen[self.row].append(s)
        self.row += 1
    

class Device:
    def __init__(self):
        self.CPU = CPU()
        self.CRT = CRT()
        
    def redraw(self, cycle_count):
        return cycle_count % 40 == 0

    def process(self, cmd):
        cmd = cmd.split(' ')
        redraw = False
        cycle_count = len(self.CPU.cycles)
        if cmd[0] == 'noop':
            self.CPU.noop()
            cycle_count += 1 
            redraw = self.redraw(cycle_count)
        elif cmd[0] == 'addx':
            self.CPU.addx(int(cmd[1]))
            cycle_count += 1 
            redraw = self.redraw(cycle_count)
            cycle_count += 1 
            if False == redraw:
                redraw = self.redraw(cycle_count) 
        if redraw == True:
            start = self.CRT.row * 40
            end = start + 40
            cycles = self.CPU.cycles[start:end]
            self.CRT.draw(cycles)


INPUT = sys.argv[1] if len(sys.argv) >= 2 else 'test'

device = Device()

f = open(INPUT, 'r')
input = f.readlines()

answer_pt1 = 0
cycles = [20, 60, 100, 140, 180, 220]
for cmd in input:
    device.process(cmd.strip())

for i,x in enumerate(cycles):
    answer_pt1 += device.CPU.signal_strength(x)
print('Signal strength:', answer_pt1)

for row in device.CRT.screen:
    screen=''
    for pixel in device.CRT.screen[row]:
        screen = "{r}{p}".format(r=screen, p=pixel)
    print(screen)