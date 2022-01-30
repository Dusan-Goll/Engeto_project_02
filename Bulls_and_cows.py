import time
import pprint

import BC_added_functions as BCf

separator = '-' * 42
doublesep = '=' * 42
stats = {}

print("\n------^v^----< BULLS & COWS >----^v^------\n"
      "\nHello there, welcome to the game."
      "\nI'll generate random 4-digit number,"
      "\nyour job is to guess the number."
      "\n" + separator)
print("RULES:\n"
      "1/ The Secret number:\n"
      "\ta) has 4 digits\n"
      "\tb) doesn't start with zero\n"
      "\tc) has no digit repeated.\n"
      "2/ One 'bull' for every digit\n"
      "   you hit in the Secret number.\n"
      "3/ One 'cow' for every miss-positioned\n"
      "   digit in the Secret number.\n"
      f"{separator}"
      )
player_name = input("Write your Player name and start the game. ->  ")

stats[f'player: {player_name}'] = {}
want_to_game = True
game = 0
while want_to_game:
    game = game + 1
    print(f"{doublesep}\nround {game}")
    Number = BCf.rand4dig()
    attempts = 0
    guessing = True
    starttime = time.time()
    while guessing:
        print(separator)
        guess = input("Guess the number: ")
        if BCf.inputcheck(guess) == 'OK':
            attempts += 1
            if guess == Number:
                roundtime = round((time.time() - starttime)/60, 1)
                guessing = False
            else:
                BCf.bulls_cows(guess, Number)

    if guessing is False:
        print(f"You WIN !\n{attempts} attempt(s) in {str(roundtime)} min")
        g_rating = BCf.gamerating(attempts, roundtime)
        print(g_rating)
        print(f"\n{doublesep}")

        round_stat = (g_rating, attempts, str(roundtime))
        stat_string = f'{{0:^15}}, ' \
                      f'{{1:>2}} attempts in {{2:>5}} min'.format(*round_stat)
        round_num = game if game > 9 else f'0{game}'
        round_str = f'round {round_num:>2}'
        stats[f'player: {player_name}'][round_str] = stat_string

        asking = input("Do you wanna play one more round? y/n ->")
        if asking == 'y':
            continue
        else:
            want_to_game = False
            print(f'{doublesep}\ngame statistics:')
            pprint.pprint(stats)
