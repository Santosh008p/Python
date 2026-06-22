secret_number=7
guess_limit=3
guess_count=0
while guess_count<guess_limit:
    guess=int(input("Guess the secret number:"))
    guess_count +=1
    if guess==secret_number:
        print("Congratualations, You Win!")
    else:
        print("Oops!, try again")
        break

print("Your are out of guess, you lose!")