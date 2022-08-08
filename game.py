import random

user_points = 0 
computer_points = 0

options = ["r", "p", "t"]

name_user = input("Digite o seu nickname: ")

#Rock, paper and scissors
while True:
    user_choice = input("Escolha: [R] (Pedra) | [P] (Papel) | [T] (Tesoura) | [S] para sair. ").lower()

    if user_choice == "s":
        break
    
    if user_choice not in options:
        print("Inválido!")
        continue

    computer_choice = random.randint(0, 2)  
    # 0:R, 1:P, 2:T

    computer_option = options[computer_choice]

    print("O computador escolheu " + computer_option)

    if user_choice == computer_option:
        print("Empate!")
    elif user_choice == "r" and computer_option == "t":
       print("Parabéns, você ganhou!") 
       user_points = user_points + 1

    elif user_choice == "p" and computer_option == "r":
        print("Parabéns, você ganhou!")
        user_points = user_points + 1

    elif user_choice == "t" and computer_option == "p":
         print("Parabéns, você ganhou!")
         user_points = user_points + 1
    
    else:
        print("Ih, você foi derrotado!")
        computer_points = computer_points + 1
    

print("Sua pontuação: " + str(user_points))
print("Pontuação do Computador: " + str(computer_points))

if user_points > computer_points:
    print("Parabéns, " + name_user + "! Você venceuu :)")
elif user_points == computer_points:
    print("Empate!")
else: 
    print("Você foi derrotado (a), " + name_user + "!")


print("Tchauuuu, até mais!")


