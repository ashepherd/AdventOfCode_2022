import sys

INPUT = 'input'

class CPU:
    def __init__(self):
        self.X = 1
        self.cycles = [0]

    def process(self, cmd):
        cmd = cmd.split(' ')
        if cmd[0] == 'noop':
            self.noop()
        elif cmd[0] == 'addx':
            self.addx(int(cmd[1]))
        return len(self.cycles)

    def addx(self, value):
        cost = 2 #cycles
        self.cycles.append(self.X)
        self.X += value        
        self.cycles.append(self.X)

    def noop(self):
        cost = 1 #cycle
        self.cycles.append(self.X)

    def signal_strength(self, cycle):
        i = cycle - 1
        return self.cycles[i] * cycle

class ClockCircuit:
    def __init__(self):
        self.CPU = CPU()


INPUT = sys.argv[1] if len(sys.argv) >= 2 else 'test'
print(INPUT)

cpu = CPU()
f = open(INPUT, 'r')
input = f.readlines()

answer_pt1 = 0
cycles = [20, 60, 100, 140, 180, 220]
for cmd in input:
    num_cycle = cpu.process(cmd.strip())
    #print(num_cycle, cpu.X)

for i,x in enumerate(cycles):
    ss = cpu.signal_strength(x)
    print(x, ss)
    answer_pt1 += ss
print(answer_pt1)


#for i,x in enumerate(cpu.cycles):
#    print(i, x)