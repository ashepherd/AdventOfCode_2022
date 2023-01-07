import json

file1 = open('input.csv', 'r')
Lines = file1.readlines()

 
counter = {}
section = 0
counter[section] = 0
largest = 0
# Strips the newline character
for line in Lines:
    stripped_line = line.strip()
    if not stripped_line:
        if largest < counter[section]:
            largest = counter[section]
        section += 1
        counter[section] = 0
    else:
        counter[section] += int(stripped_line)

sorted_dict = sorted(counter.items(), key=lambda item: item[1])
#print(json.dumps(sorted_dict, sort_keys=True, indent=4))
print (largest)

top_three = sorted_dict[-3:]
#print(json.dumps(top_three, sort_keys=True, indent=4))
top_three_val = 0
for id,val in top_three:
    top_three_val += val
    print(val)

print (top_three_val)