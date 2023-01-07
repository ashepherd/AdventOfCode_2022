#INPUT = 'test'
INPUT = 'input'

def column(matrix, i):
    return [matrix[row][i] for row in matrix]

class Tree:
    def __init__(self, row, col, value):
        self.pos = {'row': row, 'col': col}
        self.value = value
        
    def directional_scenic_score(self, label, value, arr, start, end, step):
        score = 0
        hidden = False
        for i in range(start, end, step):
            score += 1
            if arr[i] >= value:
                hidden = True
                break
        return score, hidden

    def calculate(self, row, col):
        left_score, left_hidden = self.directional_scenic_score(label='left', value=self.value, arr=row, start=self.pos['col']-1, end=0-1, step=-1)
        right_score, right_hidden =self.directional_scenic_score(label='right', value=self.value, arr=row, start=self.pos['col']+1, end=len(row), step=1)
        top_score, top_hidden =self.directional_scenic_score(label='top', value=self.value, arr=col, start=self.pos['row']-1, end=0-1, step=-1)
        bottom_score, bottom_hidden =self.directional_scenic_score(label='bottom', value=self.value, arr=col, start=self.pos['row']+1, end=len(col), step=1)
        score = left_score * right_score * top_score * bottom_score
        visible = left_hidden is False or right_hidden is False or top_hidden is False or bottom_hidden is False
        return score, visible

f = open(INPUT, 'r')
grid = f.readlines()

trees = {}

for id,row in enumerate(grid):
    trees[id] = []
    for i,t in enumerate(row.strip()):
        trees[id].append(t)

answer_pt1 = len(trees[0]) + len(trees[list(trees)[-1]])
last_row_id = list(trees)[-1]

answer_pt2 = 0

for i in range(1,last_row_id):
    for idx, tree in enumerate(trees[i]):

        # count the edges as visible
        if idx == 0 or idx == len(trees[i])-1:
            answer_pt1 += 1
            continue

        # in the middle of the grid
        else:
            t = Tree(row=i, col=idx, value=tree)
            score, visible = t.calculate(row=trees[i], col=column(matrix=trees, i=idx))
            if visible:
                answer_pt1 += 1
            if score > answer_pt2:
                answer_pt2 = score       

print('Answer #1: ', answer_pt1)
print('Answer #2: ', answer_pt2)
