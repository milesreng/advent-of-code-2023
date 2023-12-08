

with open('data/day2.txt') as f:

  count = 0

  for game in f:
    game_id, results = game.strip().split(":")
    game_id = int(game_id.split(" ")[1])

    subsets = results.split(";")
    valid = True

    # green, red, blue
    for set in subsets:
      quantities = set.strip().split(",")

      for amt in quantities:
        num, color = amt.strip().split(" ")
        if color == "green" and int(num) > 13:
          valid = False
        elif color == "red" and int(num) > 12:
          valid = False
        elif color == "blue" and int(num) > 14:
          valid = False

    if valid:
      count += game_id

  print(count)