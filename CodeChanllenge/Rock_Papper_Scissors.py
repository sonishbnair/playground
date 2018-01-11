print("Rock, Paper, Scissors. Rules - Rock beats scissors, Scissors beats paper, Paper beats rock")
#Truth table, if P1=rock & P2=scissors then P1 winds. If P1=scissors & P2=rock then P2 wins
#https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/assignments/MIT6_189IAP11_hw1.pdf
rps = {"rock":"scissors", "scissors":"paper", "paper":"rock"}

while True:
    Player_1 = raw_input("Player 1:").strip().lower()
    Player_2 = raw_input("Player 2:").strip().lower()
    if Player_1 in rps.values() and Player_2 in rps.values():
        break
    else:
        print "Invalid input, accepted values are Rock, Paper and Scissors"

if Player_1 == Player_2:
    print "Tie"
elif rps[Player_1] == Player_2:
    print "Player 1"
elif rps[Player_2] == Player_1:
    print "Player 2"
