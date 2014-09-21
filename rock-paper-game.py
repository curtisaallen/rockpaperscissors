import random
weapon = ['PAPER','ROCK','SCISSORS']

num = random.choice(range(0, 2))

while True:
    print("You have enter the paper rock scissors battle game")
    print("choose your weapon wisely")
    print("Your weapon choose are: PAPER, ROCK, SCISSORS")
    print("Enter QUIT to quit")
    
    choose = input()
    choose = choose.upper()
       
    if choose == 'QUIT':
        break
      
    if choose == weapon[num]:
        print("Player and computer tie!")
        break
    else:
        if choose == 'PAPER':
            print("Player chooses %s"%choose)
            print("Computer chooses %s"%weapon[num])
            if weapon[num] == 'ROCK':
                print("Player wins!")
            else:
                print("Computer wins!")
            break
        if choose == 'ROCK':
            print("Player chooses %s"%choose)
            print("Computer chooses %s"%weapon[num])
            if weapon[num] == 'PAPER':
                print("Computer wins!")
            else:
                print("Player wins!")
            break
        if choose == 'SCISSORS':
            print("Player chooses %s"%choose)
            print("Computer chooses %s"%weapon[num])
            if weapon[num] == 'ROCK':
                print("Computer wins!")
            else:
                print("Player wins!")
            break
            