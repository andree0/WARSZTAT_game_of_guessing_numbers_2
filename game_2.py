print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbkach")
go = input("and press ENTER")
min = 0
max = 1000
answer_options = ['too big', 'too small', 'you win']

while True:
    guess = int((max - min) / 2) + min

    print("Zgaduję: ", guess)

    answer = input("Jaka jest twoja odpowiedź (Too small/Too big/You win)")
    answer = answer.lower()

    if answer not in answer_options:
        print('zła odpowiedź')
    elif answer == 'you win':
        print("Wygrałeś!")
        break
    elif answer == 'too big':
        max = guess
    elif answer == 'too small':
        min = guess

    if min == max:
        print('nie oszukuj!')
