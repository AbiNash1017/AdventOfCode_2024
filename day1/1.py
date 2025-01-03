from collections import Counter
a,b=[],[]
with open('D:/Advent of code/day1/input.txt', 'r') as f:
   for line in f.readlines():
      x,y=(int(z) for z in line.split())
      a.append(x)
      b.append(y)
#part1
a.sort()
b.sort()
print(a)
print(b)

n=len(a)
print('\nthe solution for part 1:\t')
print(sum(abs(a[i]-b[i]) for i in range(len(a))))
print('----------------------------------------------------------------------------------------------------------------------')
#part2
c=Counter(b)
print(c)
print('\nthe solution for part 2:\t')
print(sum(a[i]*c[a[i]] for i in range(n)))