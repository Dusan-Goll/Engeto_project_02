from random import choice


def rand4dig():
    """Returns random 4-digit number. Digits in the number are unique
    and first digit isn't zero."""
    digits = list(range(1, 10))
    number = str(digits.pop(digits.index(choice(digits))))
    digits.append(0)
    for num in range(3):
        number = number + str(digits.pop(digits.index(choice(digits))))
    return number


def inputcheck(inp):
    """Checks player's input. Returns announcement, if it's out of 'bounds'"""
    if not str(inp).isdigit():
        return print("The input isn't whole of digits.")
    elif len(str(inp)) > 4:
        return print("The number has more than 4 digits.")
    elif len(str(inp)) < 4:
        return print("The number has less than 4 digits.")
    elif str(inp).startswith('0'):
        return print("First digit of the number is zero.")
    else:
        for i in range(len(inp)):
            if inp[i] in (inp[0:i] + inp[i+1:]):
                return print('Some digit is repeated in the number.')
        else:
            return 'OK'


def bulls_cows(shot, secret_num):
    """Returns numbers of Bulls and Cows of player's shot."""
    bulls, cows = 0, 0
    for idx in range(4):
        if shot[idx] == secret_num[idx]:
            bulls = bulls + 1
        elif shot[idx] in secret_num:
            cows = cows + 1
    if bulls == 1:
        bullword = "bull"
    else:
        bullword = "bulls"
    if cows == 1:
        cowword = "cow"
    else:
        cowword = "cows"
    return print(f"{bulls} {bullword}, {cows} {cowword}")


def gamerating(attempts_num, round_time):
    """Returns round rating."""
    if attempts_num == 1:
        rating = '*!"BOMBASTIC"*!'
    elif 1 < attempts_num <= 5 or round_time < 1.5:
        rating = '"!EXCELLENT!"'
    elif (5 < attempts_num <= 10) or round_time < 2:
        rating = '"GREAT"'
    elif (10 < attempts_num <= 13) or round_time < 2.5:
        rating = '"GOOD"'
    elif (13 < attempts_num <= 16) or round_time < 3:
        rating = '"NOT BAD"'
    else:
        rating = '"AVERAGE"'
    return rating
