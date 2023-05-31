import random

options = ['rock', 'paper', 'scissors']
#          0     1      2
choices = options[:]
chance = [10,10,10]
# which option beats which
def thinker (ply, comp):
    result = options.index(ply) - options.index(comp)
    result = result % 3
    #print(chance)
    if result == 1:
        print("You won!")
        if chance [options.index(comp)] > 1:    
            chance[options.index(comp)] = chance[options.index(comp)] - 1
    elif result == 2:
        print("I Won!")
        chance[options.index(comp)] = chance[options.index(comp)] + 1
    elif result == 0:
        print("It's a Tie!")
    #return result #1 = player W, 2 = player L, 0 = T

#play instructions
print("let's play Rock Paper Scissors")
print("Rock smashes scissors, Paper covers rock, Scissors cut paper ")

while True:
    #randomly choose one
    compchoice = random.choice(choices)

    #get input
    plychoice = ""
    while plychoice not in options:
        plychoice = input("pick one (rock, paper, or scissors): ")
        plychoice = plychoice.lower()

    print("You picked", plychoice,"and I picked",compchoice)
    thinker(plychoice, compchoice)
