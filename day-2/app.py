import json

dict = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissor'
}

score_key = {
    'A': 1,
    'B': 2, 
    'C': 3,
}

win = 6
draw = 3
loss = 0


def calculate_score(result, type):
    return result + type

def round_result_value(opponent, you, dict):

    if you not in score_key:
        raise Exception("Unknown input: " + you)

    if opponent == you:
        return calculate_score(result=draw, type=score_key[you]), draw
    elif dict[opponent] == 'Rock' and dict[you] == 'Paper':
        return calculate_score(result=win, type=score_key[you]), win
    elif dict[opponent] == 'Rock' and dict[you] == 'Scissor':
        return calculate_score(result=loss, type=score_key[you]), loss
    elif dict[opponent] == 'Paper' and dict[you] == 'Rock':
        return calculate_score(result=loss, type=score_key[you]), loss
    elif dict[opponent] == 'Paper' and dict[you] == 'Scissor':
        return calculate_score(result=win, type=score_key[you]), win
    elif dict[opponent] == 'Scissor' and dict[you] == 'Rock':
        return calculate_score(result=win, type=score_key[you]), win
    elif dict[opponent] == 'Scissor' and dict[you] == 'Paper':
        return calculate_score(result=loss, type=score_key[you]), loss
    else:
        raise Exception("Unknown battle: " + opponent + ' vs. ' + you)

def rock_paper_scissor(Lines):
    scenario = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    total_score = 0
    for line in Lines:
        stripped_line = line.strip()
        round = stripped_line.split()
        
        opponent = round[0]
        you = scenario[round[1]]
        (score, wlod) = round_result_value(opponent=opponent, you=you, dict=dict)
        total_score += score
    return total_score

def win_lose_or_draw(Lines):
    scenario = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
    total_score = 0
    for line in Lines:
        stripped_line = line.strip()
        round = stripped_line.split()
        
        opponent = round[0]
        result = scenario[round[1]]
        if result == 'win':
            total_score += win
            if opponent == 'A':
                total_score += score_key['B']
            elif opponent == 'B':
                total_score += score_key['C']
            else:
                total_score += score_key['A']
        elif result == 'lose':
            total_score += loss
            if opponent == 'A':
                total_score += score_key['C']
            elif opponent == 'B':
                total_score += score_key['A']
            else:
                total_score += score_key['B']
        else:
            total_score += draw
            total_score += score_key[opponent]
    return total_score


file1 = open('input', 'r')
Lines = file1.readlines()

total = rock_paper_scissor(Lines=Lines)
print(total)

wld = win_lose_or_draw(Lines=Lines)
print(wld)

