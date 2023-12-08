import re

file = open('data/day1.txt', 'r')

def part1():
  sum = 0 

  for line in file:
    digits = re.findall(r'\d', line)
    print(digits)
    num = str(digits[0]) + str(digits[-1])

    sum += int(num)

  print(sum)
  return

def part2():
  
  return

file.close()