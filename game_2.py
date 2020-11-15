print("Imagine number between 0 and 1000, I will guess the number in 10 tries")
go = input("and press ENTER")
user_min = 0
user_max = 1000
answer_options = ['too big', 'too small', 'you win']

while True:
    guess = int((user_max - user_min) / 2) + user_min

    print(f"It is number {guess}")

    answer = input()
    answer = answer.lower()
    if user_min == user_max or user_min == guess - 1:
        print('not cheat!')
    else:

        if answer not in answer_options:
            print('wrong answer')
        elif answer == 'you win':
            print("You win!")
            break
        elif answer == 'too big':
            user_max = guess
        elif answer == 'too small':
            user_min = guess
