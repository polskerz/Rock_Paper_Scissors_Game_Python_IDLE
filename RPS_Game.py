import random
import csv
    
def play_game():
    global n, username
    username = input("\nEnter your username:")
    n = int(input("\nEnter total limit of attempts:"))
    print("\nThe game begins!")

    u_win_count = 0
    u_loss_count = 0
    u_tie_count = 0

    for i in range(n):
        print("\n\tAttempt" + ' ' + '#' + str(i + 1))
        u_choice = get_u_choice()
        c_choice = get_c_choice()
        print()
        print('Computer chose' + ' ' + str(c_choice) + '.') 
        print('You chose' + ' ' + str(u_choice) + '.')
        u_win_count, u_loss_count, u_tie_count = game_result(c_choice, u_choice, u_win_count, u_loss_count, u_tie_count)

    print("You won" + ' ' + str(u_win_count) + ' ' + "out of" + ' ' + str(n) + ' ' + "attempts!")
    print("\nSave game progress?")
    c=input("Enter your choice [y/n]:")
    
    while c != 'y' and c!= 'n':
        print('Error. The valid choices are y or n')
        c = input("Please enter a valid option:")
    if c == 'y' :
            print()
            update_progress(n, u_win_count, u_loss_count, u_tie_count, username)
    else:
        print()
        print("Progress not saved.")
    
        
def get_u_choice():
    print("\nSelect from the following options:")
    print("1 for ROCK")
    print("2 for PAPER")
    print("3 for SCISSORS")
    choice = int(input("Enter your choice:"))

    while choice != 1 and choice != 2 and choice != 3: 
        print('Error. The valid choices are rock(type in 1),') 
        print('paper(type in 2), or scissors(type in 3).') 
        choice = int(input('Please enter a valid choice: ')) 

    if choice == 1: 
        choice = 'ROCK' 
    elif choice == 2: 
        choice = 'PAPER' 
    else: 
        choice = 'SCISSORS' 

    return choice 

      
def get_c_choice():
    choice = random.randint(1,3) 
    if choice == 1: 
        choice = 'ROCK' 
    elif choice == 2: 
        choice = 'PAPER' 
    else: 
        choice = 'SCISSORS'
        
    return choice      
       
def game_result(c_choice, u_choice, u_win_count, u_loss_count, u_tie_count):
    
    if c_choice == u_choice:
        u_tie_count += 1
        print("It's a tie!")
    elif c_choice == 'SCISSORS' and u_choice == 'ROCK':
        u_win_count += 1
        print('ROCK crushes SCISSORS! You win!')
    elif c_choice == 'PAPER' and u_choice == 'SCISSORS': 
        u_win_count += 1
        print('SCISSORS cut PAPER! You win!')
    elif c_choice == 'ROCK' and u_choice == 'PAPER': 
        u_win_count += 1
        print('PAPER covers ROCK! You win!')
    else: 
        u_loss_count += 1
        print('You lose!')
    print()
    return u_win_count, u_loss_count, u_tie_count

def update_progress(n, u_win_count, u_loss_count, u_tie_count, username):
    f = open("RPS_Scoreboard.csv")
    a = csv.reader(f)
    flag = 0
    for i in a:
        if username == i[0]:
            flag = 1
    f.close()

    if flag == 1:
        f1 = open("RPS_Scoreboard.csv", 'r+', newline='')
        a1 = csv.reader(f1)
        t = list(a1)
        f1.seek(0)
        a12 = csv.writer(f1)
        for j in t:
            if j[0] == str(username):
                j[1] = str(int(j[1]) + int(u_win_count))
                j[2] = str(int(j[2]) + int(u_loss_count))
                j[3] = str(int(j[3]) + int(u_tie_count))
                j[4] = str(int(j[4]) + int(n))
                slice1 = str(float(j[1])/float(j[4]))
                ratio1 = slice1[:5]
                j[5] = str(ratio1)
                break
        a12.writerows(t)
        print("Progress saved!")
        f1.close()
          
    else:
        f = open("RPS_Scoreboard.csv", 'a', newline='')
        r = csv.writer(f)
        slice2 = str(float(u_win_count/n))
        ratio2 = slice2[:5]
        r.writerow([str(username), str(u_win_count), str(u_loss_count), str(u_tie_count), str(n), str(ratio2)])
        print("Username added, progress saved!")
        f.close()

      
def view_scoreboard():
    f = open("RPS_Scoreboard.csv")
    a = csv.reader(f)
    print()
    print("All-Time Leaderboard\n")
    x = next(a)
    print(x)
    num = []
    for i in a:
        num.append(float(i[5]))
    num.sort(reverse=True)
    for i in num:
        f.seek(0)
        a1 = csv.reader(f)
        x1 = next(a)
        for j in a1:
            if float(j[5]) == float(i):
                print(j)

print("\t\t########## ROCK, PAPER & SCISSORS ##########\n")
print("Select one of the options to get started:")
while True:
    print("\n1.Play the game")
    print("2.View Scoreboard")
    print("3.Exit\n")
    ch = int(input("Enter your choice:"))
    
    if ch == 1:
        play_game()
        
    elif ch == 2:
        view_scoreboard()
         
    elif ch==3:
        print()
        print("Exiting...")
        print("Credits: Paul Binu")
        break

    


           
    
    
