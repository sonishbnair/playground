import random

def getRandomNum():
    return random.randint(0,9)

def main():
    count = 0
    print "Guess a number between 0-9... Type exit to stop guessing"
    randomNum=getRandomNum()

    while True:
        userInput = raw_input("Number you are guessing:")
        if userInput.lower() == 'exit':
            #print("Random number was %s. Number of attempt %s" % (randomNum, numGuessed))
            print "Exiting... Random num:" , randomNum , "Number of attempt:" , count
            break
        numGuessed = int(userInput.strip())

        if numGuessed == randomNum:
            print "Congratulation Number you guessed is correct. Number of attempt:" , count
            break
        elif numGuessed < randomNum:
            print "Number guessed is too low"
        elif numGuessed > randomNum:
            print "Number guessed is too high"
        count += 1
        
if __name__ == '__main__':
    main()
