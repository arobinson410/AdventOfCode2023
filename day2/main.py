
# A game is possible iff draws from bag are <= 12 red, <= 13 green, and <= 14 blue
if __name__ == '__main__':

    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    game_sum = 0

    # Get inputs from file
    with open('puzzle_input.txt', 'r') as puzzle_input:
        puzzle_inputs = puzzle_input.readlines()

    for line in puzzle_inputs:

        # Parse string to get information 
        # tokens[0] is game number
        # tokens[1] is the pulls
        tokens = line.split(':')

        game_number = tokens[0].strip()
        game_pulls = tokens[1].strip().split(';')

        print(game_number)

        game_rolls = []

        # Get list of games
        for game in game_pulls:

            colors = game.split(', ')
            colors = [x.strip() for x in colors]
            
            color_dict = {'red': 0, 'green': 0, 'blue': 0}

            for color in colors:

                # color_tokens[0] is count
                # color_tokens[1] is color
                color_tokens = color.split()

                color_dict[color_tokens[1]] = int(color_tokens[0])

            game_rolls.append(color_dict)

        print(game_rolls)

        is_game_possible = True

        for pull in game_rolls:

            if not(pull['red'] <= MAX_RED and pull['blue'] <= MAX_BLUE and pull['green'] <= MAX_GREEN):

                is_game_possible = False
                break

        if is_game_possible:

            game_sum += int(game_number.split()[1])

        print(is_game_possible)
        #exit(0)

    print(game_sum)