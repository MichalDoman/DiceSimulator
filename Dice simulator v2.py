from random import randint


def main():
    print('-------------------------------------------------------------')
    print('         Welcome to the Dice Throwing Simulator! ')
    print('-------------------------------------------------------------')
    print('')

    score = simulate_throws()
    print(f'Your score was: {score}!')


def interpret_code():
    """Takes user input in form of a die code, checks its correctness, and interprets it.

    :return: information gotten from the code (number of throws, type of dice & value of the modifier).
    """

    while True:
        code = input('Type in the code and the system will generate the moves: ')
        try:
            # This part checks if the code has a proper amount of non-digits:
            count = 0
            for character in code:
                if not character.isdigit():
                    count += 1
            if count > 2:
                raise ValueError

            first_split = code.upper().split('D')
            if first_split[1] == '':
                raise ValueError

            number_of_throws = first_split[0]
            if number_of_throws == '' or int(number_of_throws) < 1:
                number_of_throws = 1

            modifier = 0
            second_split = first_split[1]
            dice_size = second_split
            for character in first_split[1]:
                if not character.isdigit():
                    second_split = first_split[1].split(character)
                    if character == '-':
                        modifier = -int(second_split[1])
                    else:
                        modifier = int(second_split[1])
                    dice_size = second_split[0]

            return number_of_throws, dice_size, modifier

        except (ValueError, IndexError, TypeError):
            print('This is not a valid code')
            print('')
            continue


def simulate_throws():
    """Simulates throws according to the given code

    :return: prints the throws and returns their total value
    """

    number_of_throws, dice_size, modifier = interpret_code()

    total_score = 0
    for throw in range(int(number_of_throws)):
        throw_outcome = randint(1, int(dice_size))
        print(f'Throw number {throw + 1}: {throw_outcome}')
        total_score += throw_outcome
    total_score += modifier
    return total_score


if __name__ == '__main__':
    main()
