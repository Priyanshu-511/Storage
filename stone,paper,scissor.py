import random
user = input("Choose any one: stone, paper, scissor: ").lower()
computer = random.randint(0,2)

dic = {
    0: "stone",
    1: "paper",
    2: "scissor"
}

if user in dic.values():
    if (user == 'stone' and dic[computer] == 'scissor') or \
       (user == 'paper' and dic[computer] == 'stone') or \
       (user == 'scissor' and dic[computer] == 'paper'):
        print(f"You chose {user}. Computer chose {dic[computer]}. You win!")
    elif user == dic[computer]:
        print(f"Both chose {user}. It's a tie!")
    else:
        print(f"You chose {user}. Computer chose {dic[computer]}. Computer wins!")
else:
    print("Invalid choice. Please choose stone, paper, or scissor.")
