import re
data=[]

with open('D:/Advent of code/day3/input.txt', 'r') as f:
    data = f.read()

pattren= r'mul\(\d\d?\d?,\d\d?\d?\)'

def get_result(s):
    result=0
    for m in re.findall(pattren,s):
        l,r=m.split(',')
        result+=int(l[4:])*int(r[:-1])
    return result
print('part 1: ',get_result(data))

clean_data=[]
i=0
do=True
while i<len(data):
    if do:
        if data[i:i+5]=='don\'t':
            do=False
            i+=5
        else:
            clean_data.append(data[i])
            i+=1
    else:
        if data[i:i+2]=='do' and data[i:i+5] !='don\'t':
            do=True
            i+=2
        else:
            i+=1

clean_data=''.join(clean_data)
print('part 2: ',get_result(clean_data))