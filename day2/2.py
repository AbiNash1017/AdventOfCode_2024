rerports=[]
with open('D:/Advent of code/day2/input.txt', 'r') as f:
   for line in f.readlines():
      rerports.append([int(z) for z in line.split()])

def is_safe(l):
    n=len(l)
    return all(1<=l[i+1]-l[i]<=3 for i in range(n-1)) or(all(1<=l[i]-l[i+1]<=3 for i in range(n-1)))
#part-1
safe_count=sum(map(is_safe,rerports))
print('\nthe solution for part 1:\t')
print(safe_count)

#part-2
safe_count2=0
for report in rerports:
   safe_count2+=(is_safe(report) or any(is_safe(report[:i]+report[i+1:]) for i in range(len(report))))
print('\nthe solution for part 2:\t')
print(safe_count2)