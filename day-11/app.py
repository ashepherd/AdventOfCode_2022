import sys

class Monkey:
    def __init__(self, id):
        self.id = id
        self.items = []
        self.operator = None
        self.op_value = None
        self.test = None
        self.yes_monkey = None
        self.no_monkey = None
        self.activity = 0

    def set_items(self, items):
        self.items = items

    def set_op(self, op, value):
        self.operator = op
        self.op_value = value
    
    def set_test(self, t):
        self.test = int(t)

    def set_test_true(self, y):
        self.yes_monkey = y

    def set_test_false(self, n):
        self.no_monkey = n

    def run_op(self, item):
        value = self.op_value
        if value.isnumeric():
            value = int(value)
        elif value == 'old':
            value = item

        if self.operator == '*':
            return item * value
        elif self.operator == '+':
            return item + value
    
    def run_test(self, item):
        if item % self.test == 0:
            return self.yes_monkey
        else:
            return self.no_monkey

    def get_bored(self, item):
        return item // 3

    def inspect(self):
        throws = []
        while self.items:
            item = int(self.items.pop(0))
            self.activity += 1
            worry = self.run_op(item)
            worry = self.get_bored(worry)
            target = self.run_test(worry)
            throws.append({'target': target, 'item': worry})
        return throws

    def catch(self, item):
        self.items.append(item)


def iterate(monkeys):
    for m in monkeys:
        monkey = monkeys[m]
        items = monkey.inspect()
        for toss in items:
            monkeys[toss['target']].catch(toss['item'])

def find_active_monkeys(monkeys):
    active = []
    for m in monkeys:
        active.append(monkeys[m].activity)
    active.sort(reverse=True)
    top_two = active[0:2]
    return top_two[0] * top_two[1]

INPUT = sys.argv[1] if len(sys.argv) >= 2 else 'test'
f = open(INPUT, 'r')
input = f.readlines()

monkeys = {}
monkey = None
for line in input:
    line = line.strip()
    if line.startswith('Monkey '):
        if None is not monkey:
            monkeys[monkey.id] = monkey

        monkey = Monkey(line.split(':')[0].split(' ')[1])
        continue
    elif line.startswith('Starting items:'):
        monkey.set_items(line.split(':')[1].strip().replace(" ", "").split(','))
        continue
    elif line.startswith('Operation: new = old '):
        op = line.split('new = old ')[1].split(' ')
        monkey.set_op(op=op[0], value=op[1])
        continue
    elif line.startswith('Test:'):
        monkey.set_test(line.split(' by ')[1])
        continue
    elif line.startswith('If true'):
        monkey.set_test_true(line.split(' monkey ')[1])
        continue
    elif line.startswith('If false'):
        monkey.set_test_false(line.split(' monkey ')[1])
        continue

if None is not monkey:
    monkeys[monkey.id] = monkey

for i in range(0, 20):
    iterate(monkeys)
answer_pt1 = find_active_monkeys(monkeys)
print('Answer #1:',answer_pt1)


