import random
commands={
    # thing:['beats']
    'rock':['scissor','paper'],
    'paper':['rock','scissor'],
    'scissor':['paper','rock']
}
def getInput():
    commandUser=input('Rock Paper Scissor?\nEnter input:')
    commandUser=commandUser.lower()
    if(commandUser not in commands):
        if(commandUser.lower() == 'fire'):
            print("Water balloon I win")
        else:
            print('Please enter a valid command (Rock Paper or Scissor)')
            getInput()
    else:
        commandComputer=random.choice(list(commands.keys()))
        if(commandComputer.lower() == commandUser):
            print("It's a TIE\ntry again")
            getInput()
        elif(commandComputer==commands[commandUser][1]):
            print('You win {} beats {}'.format(commandUser,commandComputer))
        else:
            print('You loss {} beats {}'.format(commandComputer,commandUser))

getInput()