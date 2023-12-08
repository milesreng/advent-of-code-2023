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

with open('data/day1.txt') as f:
  digits = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
  print(sum([int(digits.get(v[0], v[0]) + digits.get(v[-1], v[-1])) for v in [re.findall(f"(?=(\d|{'|'.join(digits.keys())}))", l) for l in f]]))

file.close()