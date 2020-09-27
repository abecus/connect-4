#%%
import board


game = board.Board()
player = {1:'Red', 0:'Yellow'}

def play():
    while not game.over:
        s = input(f"Player {player[game.turn]} | Enter Column:  ")
        if s.isdigit():
            out = game.drop(int(s))
            if out != False:
                print(game)

                if out == True:
                    print('Valid Move')
                else:
                    print(out)
                
                print('_'*25, end='\n')

            else:
                print("Invalid Move")

        elif s=='START':
            print('READY')
            game.reset()

def init():
    print("Listening... ")
    while 1:
        print('Type "START", for a new game.')
        s = input()
        if  s == "START":
            print('READY')
            print(' ')
            play()

init()
# %%