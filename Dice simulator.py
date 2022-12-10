def main():
    print('-------------------------------------------------------------')
    print('         Welcome to the Dice Throwing Simulator! ')
    print('Choose the type of dice and the number of throws to generate:')
    print('-------------------------------------------------------------')
    print('')

    dice_type = take_user_input()[0]
    number_of_throws = take_user_input()[0]
    modifier = take_user_input()[0]

    simulate_throws(dice_type, number_of_throws, modifier)


def take_user_input():
    """A function that collects data from the user

    :return: type of dice to be used, number of throws and optionally the value of the modifier
    """

    dice_types = ['D3', 'D4', 'D6', 'D8', 'D10', 'D20', 'D100']
    dice_types_str = ', '.join(dice_types)
    print(f'Possible dice types: {dice_types_str}')

    y = input('Choose the type of dice (leave empty for "D6"): ').upper()
    if not y:
        y = 'D6'
    while y not in dice_types:
        print('')
        print('That is not a valid dice type!')
        y = input('Choose the type of dice: ').upper()

    number_chosen = False
    while not number_chosen:
        x = input('Choose the number of throws (leave empty for "1"): ')
        if not x:
            x = 1
            break
        try:
            x = int(x)
        except ValueError:
            print('')
            print('Type in a NUMBER...')
            continue
        if x == 0:
            print('')
            print("So you think your so smart huh? Try again.")
            continue
        number_chosen = True

    modifier_chosen = False
    while not modifier_chosen:
        z = input('Choose a modifier (leave empty to omit):')
        if not z:
            z = 0
            break
        try:
            z = int(z)
        except (ValueError, TypeError):
            print('')
            print('Please, type in a number or leave the choice empty.')
            continue

    return x, y, z


def simulate_throws(dice_type, number_of_throws=1, modifier=0):
    """Simulates throws with a given type of dice and returns their value.

    :param dice_type: states th type of dice (possible dices: D3, D4, D6, D8, D10, D12, D20, D100).
    :param number_of_throws: number of throws to conduct. If omitted, equals 1.
    :param modifier: an optional value that modifies the final outcome.
    :return: shows the throws and returns their value
    """


if __name__ == '__main__':
    main()
