import random

AVAILABLE = ['scissors', 'rock', 'paper']
def bot_choise():
    return AVAILABLE[random.randint(0,2)]

def who_won(user, bot):
    if AVAILABLE.index(user) == AVAILABLE.index(bot):
        return 'Draw'
    elif AVAILABLE.index(user) == 2 and AVAILABLE.index(bot) == 0:
        return 'Bot won'
    elif (AVAILABLE.index(user) == 0 and AVAILABLE.index(bot) == 2) or (AVAILABLE.index(user) > AVAILABLE.index(bot)):
        return 'Player Won'
    else:
        return 'Bot won'

def valid_input(user):
    if user in AVAILABLE:
        return True
    return False


while True:
    print('please enter one of the following: scissors, rock, paper')
    user = input()
    if valid_input(user):
        bot = bot_choise()
        print(f'bot chose {bot}')
        print(who_won(user, bot))
    else:
        print("Could`nt understand input, please try again")
