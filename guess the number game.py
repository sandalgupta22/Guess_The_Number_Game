import random


n= (random.randint(1,50))
print(n)

print(" Game Rules->\t you will only get 9 chances to guess the right number")
g=1
while(g<=9):
    imp=int(input("\nEnter your guess \n"))


    if(n>imp):
        print("Increase your no. to get to right answer \n")
    elif(n<imp):
        print("Reduce your no. to get to right answer   \n ")

    else:
        print("WHOHOOO.... CONGRATS YOU WON ")
        print("You answered it correctly in ",g,"guess")

        break
    print("number of guesses taken by you ",g)
    g=g+1
    if(g>9):
        print("SORRY YOU EXCEEDED NUMBER OF GUESSES\n")
        print("GAME OVER")

