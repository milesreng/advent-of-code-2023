

with open('data/day2.txt') as f:

  count = 0

  for game in f:
    game_id, results = game.strip().split(":")
    game_id = int(game_id.split(" ")[1])

    subsets = results.split(";")

    # green, red, blue
    minimums = [0, 0, 0]

    for set in subsets:
      quantities = set.strip().split(",")

      for amt in quantities:
        num, color = amt.strip().split(" ")
        if color == "green":
          minimums[0] = max(minimums[0], int(num))
        elif color == "red":
          minimums[1] = max(minimums[1], int(num))
        elif color == "blue":
          minimums[2] = max(minimums[2], int(num))

    power = minimums[0] * minimums[1] * minimums[2]
    count += power

  print(count)