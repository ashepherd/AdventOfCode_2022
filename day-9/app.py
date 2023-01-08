
INPUT = 'day-9/input'

UP = {'horizontal': False, 'positive': True}
DOWN = {'horizontal': False, 'positive': False}
LEFT = {'horizontal': True, 'positive': False}
RIGHT = {'horizontal': True, 'positive': True}

def get_path(input):
    if input == 'test':
        path = [
            'R 4',
            'U 4',
            'L 3',
            'D 1',
            'R 4',
            'D 1',
            'L 5',
            'R 2',
        ]
    else:
        f = open(INPUT, 'r')
        path = f.readlines()
    return path

class Snake:
    def __init__(self):
        start = (0,0)
        self.head = start
        self.tail = start
        self.diff = start
        self.provenance = {'head': [start], 'tail': [start]}

    def calculate_diff(self):
        return ((self.head[0] - self.tail[0]),(self.head[1] - self.tail[1]))

    def interpret_direction(self, direction):
        dir = UP
        if direction == 'U':
            dir = UP
        elif direction == 'D':
            dir = DOWN
        elif direction == 'L':
            dir = LEFT
        elif direction == 'R':
            dir = RIGHT
        else:
            raise Exception("Unknown direction: {d}".format(d=direction))

        move = 1
        if dir['positive'] == False:
            move = -1
            
        if dir['horizontal'] is True:
            return (move,0)        
        else:
            return (0,move)
    
    def update_head(self, new):
        self.head = new
        self.provenance['head'].append(new)

    def update_tail(self, new):
        self.tail = new
        self.provenance['tail'].append(new)

    def follow_instruction(self, instruction):
        i = instruction.split(' ')
        hops = int(i[1])
        move = self.interpret_direction(i[0])
        #print(instruction, move)

        for x in range(0,hops):
            head_pos = ((move[0] + self.head[0]), (move[1] + self.head[1]))
            self.update_head(head_pos)
            diff = self.calculate_diff()
            #print('Diff:', diff)
            if abs(diff[0]) > 1 or abs(diff[1]) > 1:
                # move tail using the last diff
                tail_pos = ((self.diff[0] + self.tail[0]), (self.diff[1] + self.tail[1]))
                #print('Tail:', self.tail, tail_pos)
                self.update_tail(tail_pos)
                self.diff = self.calculate_diff()
            else:
                self.diff = diff

snake = Snake()

path = get_path(input=INPUT)
for p in path:
    snake.follow_instruction(p.strip())
    
#print('Head:',snake.provenance['head'])
#print('Tail:',snake.provenance['tail'])
answer_pt1 = len([*set(snake.provenance['tail'])])
print('Answer #1:', answer_pt1)