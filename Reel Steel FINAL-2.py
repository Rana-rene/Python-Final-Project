import random, time, math
from random import randint
from sys import exit
###########################################################
#----------------Turn Based Variables---------------------#
###########################################################

# bot = Fighter('name', max_hp, ATK, DEF, speed, Attack_List, special)
class Fighter():
    def __init__(self, bot):
        self.name = bot[0]
        self.HP = HP(bot)
        self.FullHP = HP(bot)
        self.ATK= bot[2]
        self.DEF = bot[3]
        self.speed = bot[4]
        self.move1 = bot[5][0]
        self.move2 = bot[5][1]
        self.move3 = bot[5][2]
        self.move4 = bot[5][3]
        self.move5 = bot[6]
        self.Original = bot
        self.ogATK = bot[2]
        self.ogDEF = bot[3]

        
#-----------------------------------Fight action--------------------------------------

def battle(enemy_name, enemy_bot):
    opponent_name = enemy_name
    print(f"You challenged {opponent_name} to a battle!")
 
    enemydefeated = False
    counter = 4
    ironDCounter = 0
    EnemyironDCounter = 0 
    sharpenCounter = 0
    EnemysharpenCounter = 0
    while enemydefeated != True :  
        print("~" * 25)
        time.sleep(.2)
        print("{}'s HP : {}".format(player_bot.name, player_bot.HP))
        time.sleep(.2)
        print("{}'s HP : {}".format(enemy_bot.name, enemy_bot.HP))
        time.sleep(.2)
        print("What Move will you chose?")
        print()
        time.sleep(.2)
        print("1: {} \n2: {} \n3: {} \n4: {} \n5: {}".format(player_bot.move1[0],player_bot.move2[0],player_bot.move3[0],player_bot.move4[0], player_bot.move5[0]))

        MoveChoice = input()
        print("~" * 25)

        while MoveChoice not in ["1", "2", "3", "4", "5"]:
            print(player_bot.name, "doesn't understand your command!")
            MoveChoice = input()

        MoveChoice = int(MoveChoice)

        print()

        if(MoveChoice == 1):
            time.sleep(.2)
            print("{} used {}".format(player_bot.name,player_bot.move1[0]))
            Currmove = player_bot.move1
        
        if(MoveChoice == 2):
            time.sleep(.2)
            print("{} used {}".format(player_bot.name,player_bot.move2[0]))
            time.sleep(.2)
            print("{} protected itself from enemy attacks".format(player_bot.name))
            Currmove = player_bot.move2
        
        if(MoveChoice == 3):
            time.sleep(.2)
            print("{} used {}".format(player_bot.name,player_bot.move3[0]))
            Currmove = player_bot.move3
        
        if(MoveChoice == 4):
            time.sleep(.2)
            print("{} used {}".format(player_bot.name,player_bot.move4[0]))
            Currmove = player_bot.move4

        if(MoveChoice == 5):
            time.sleep(.2)
            print("{} used {}".format(player_bot.name,player_bot.move5[0]))
            Currmove = player_bot.move5
            if player_bot.move5[0] == "Weld":
                Weld(player_bot)
            elif player_bot.move5[0] == "Iron Defense":
                Iron(player_bot)
                ironDCounter = 0 
            elif player_bot.move5[0] == "Sharpen":
                Hone(player_bot)
                sharpenCounter = 0

        if MoveChoice in [1,2,3,4,5]:
            MoveChoice -= 1
            
            Damage_Taken = damage(player_bot.Original, player_bot.ATK, enemy_bot.DEF, MoveChoice)

            # Special attacks

            #accuracy check
            acc = Currmove[2]
            acc = acc*100
            acc = int(acc)
            accCheck = random.randint(0,100)
            if acc-accCheck <= 0:
                time.sleep(.2)
                print("Your Mech's move missed!")
                Damage_Taken = 0

            # Block used
            if MoveChoice == 1:
                print()
            else:
                time.sleep(.2)
                print("{} did {} to {}'s Mech.".format(player_bot.name,Damage_Taken,opponent_name))

            if enemy_bot.HP - Damage_Taken >= 0:
                enemy_bot.HP -= Damage_Taken
            else:
                enemy_bot.HP = 0

            if enemy_bot.HP == 0:
                time.sleep(.2)
                print(f"{opponent_name}'s {enemy_bot.name} was destroyed.")
                count = 0
                
        
        print()        
            # Oppoent AI
        if enemy_bot.HP>0:
            Opponent_MoveChoice = (random.choice([i for i in range(1,6) if i not in [2]]))


            if Opponent_MoveChoice == 1:
                Opponent_Move = enemy_bot.move1
        # if Opponent_MoveChoice == 2:
        #     Opponent_Move = enemy_bot.move2 
            if Opponent_MoveChoice == 3:
                Opponent_Move = enemy_bot.move3
            if Opponent_MoveChoice == 4:
                Opponent_Move = enemy_bot.move4
            if Opponent_MoveChoice == 5:
                Opponent_Move = enemy_bot.move5
            
                
            time.sleep(.2)
            print("{} used {}".format(enemy_bot.name,Opponent_Move[0]))
            # Block used
            #if Opponent_MoveChoice == 2:
                #print("{} protected itself from enemy attacks".format(player_bot.name))

            # Block Used
            if MoveChoice == 1:
                Damage_Taken = 0
                if Opponent_MoveChoice == 5:
                    if enemy_bot.move5[0] == "Weld":
                        Weld(enemy_bot)
                        time.sleep(.2)
                        print("{} did {} to your Mech".format(enemy_bot.name,Damage_Taken))
                    elif enemy_bot.move5[0] == "Rivet Gun":
                        Damage_Taken = damage(enemy_bot.Original,enemy_bot.ATK, player_bot.DEF, Opponent_MoveChoice-1)
                        Damage_Taken = 0
                        time.sleep(.2)
                        print("{} did {} to your Mech.".format(enemy_bot.name,Damage_Taken))

                else:
                    time.sleep(.2)
                    print("{} did {} to your Mech".format(enemy_bot.name,Damage_Taken))

            elif Opponent_MoveChoice == 5:
                if enemy_bot.move5[0] == "Weld":
                    Weld(enemy_bot)
                    Damage_Taken = 0
                    time.sleep(.2)
                    print("{} did {} to your Mech".format(enemy_bot.name,Damage_Taken))
                elif enemy_bot.move5[0] == "Iron Defense":
                    EnemyIron(enemy_bot)
                    EnemyironDCounter = 0 
                    Damage_Taken = 0
                    time.sleep(.2)
                    print("{} did {} to your Mech".format(enemy_bot.name,Damage_Taken))
                elif enemy_bot.move5[0] == "Sharpen":
                    EnemyHone(enemy_bot)
                    EnemysharpenCounter = 0 
                    Damage_Taken = 0
                    time.sleep(.2)
                    print("{} did {} to your Mech".format(enemy_bot.name,Damage_Taken))
                elif enemy_bot.move5[0] == "Rivet Gun":
                    Damage_Taken = damage(enemy_bot.Original,enemy_bot.ATK, player_bot.DEF, Opponent_MoveChoice-1)
                    time.sleep(.2)
                    print("{} did {} to your Mech.".format(enemy_bot.name,Damage_Taken))
                elif enemy_bot.move5[0] == "Guillotine":
                    Damage_Taken = damage(enemy_bot.Original,enemy_bot.ATK, player_bot.DEF, Opponent_MoveChoice-1)
                    time.sleep(.2)
                    print("{} did {} to your Mech.".format(enemy_bot.name,Damage_Taken))

            else:
                Damage_Taken = damage(enemy_bot.Original,enemy_bot.ATK, player_bot.DEF, Opponent_MoveChoice-1)
                time.sleep(.2)
                print("{} did {} to your Mech.".format(enemy_bot.name,Damage_Taken))

            #player_bot.HP -= Damage_Taken
            if player_bot.HP - Damage_Taken >= 0:
                player_bot.HP -= Damage_Taken
            else:
                player_bot.HP = 0
        
        player_fainted = True   
        if player_bot.HP > 0:
            ironDCounter += 1
            EnemyironDCounter += 1
            sharpenCounter += 1
            EnemysharpenCounter += 1
            player_fainted = False

        enemydefeated = True
        if enemy_bot.HP > 0 or enemy_bot.HP>0:
            enemydefeated = False

        if ironDCounter > 2:
            player_bot.DEF = player_bot.ogDEF

        if EnemyironDCounter > 2:
            enemy_bot.DEF = enemy_bot.ogDEF
        
        if sharpenCounter > 2:
            player_bot.ATK = player_bot.ogATK

        if EnemysharpenCounter > 2:
            enemy_bot.ATK = enemy_bot.ogATK

        if player_bot.HP == 0:
            time.sleep(.2)
            print()
            print(f"{PName}'s {player_bot.name} signal failed!")

        if  enemydefeated:
            time.sleep(.2)
            print(f"{PName} defeated {opponent_name}!")
            enemy_bot.DEF = enemy_bot.ogDEF
            enemy_bot.ATK = enemy_bot.ogATK
            player_bot.ATK = player_bot.ogATK
            player_bot.DEF = player_bot.ogDEF
            Heal(player_bot)
            print()

        if player_fainted:
            time.sleep(.2)
            print("Your Mech is no longer responding!\n" + PName, "Lost!")
            print()
            print(f"You have {counter} Mechs remaining.")
            counter -= 1
            if counter < 0 :
                print("""

 ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
 ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██ 
                                                                          
                 """)
                exit()
            print("You went to the Welder's Workshop and repaired your Mech")
            Heal(player_bot)
            Heal(enemy_bot)
            enemy_bot.DEF = enemy_bot.ogDEF
            enemy_bot.ATK = enemy_bot.ogATK
            player_bot.ATK = player_bot.ogATK
            player_bot.DEF = player_bot.ogDEF
            player_fainted = False
            print(f"You challenge {opponent_name} to a rematch!\n")
            print(f"{PName} has sent out {player_bot.name}")
            print(f"{opponent_name} has sent out {enemy_bot.name}")
            print()

#----------------------------------Damage Formula-----------------------------------

def damage(botATK, ATK, botDEF,moveNum):

    if moveNum == 4:
        if botATK[6][0] == 'Guillotine':
            mainDMG = ((2*50/5 +2) * botATK[6][1] *ATK/ botDEF/50)+2
            mainDMG = math.floor(mainDMG)

            return int(mainDMG)

        if botATK[6][0] == 'Iron Defense':
            mainDMG = 0
            return int(mainDMG)


        if botATK[6][0] == 'Rivet Gun':
            bulletSeed = random.randint(2,5)
            totalDMG = 0
            if bulletSeed == 2:
                for i in range(2):
                    mainDMG = ((2*50/5 +2) * botATK[6][1] *ATK/ botDEF/50)+2
                    mainDMG = math.floor(mainDMG)
                    totalDMG += mainDMG
                    print(f"You did {mainDMG} to the Mech!")
            if bulletSeed == 3:
                for i in range(3):
                    mainDMG = ((2*50/5 +2) * botATK[6][1] *ATK/ botDEF/50)+2
                    mainDMG = math.floor(mainDMG)
                    totalDMG += mainDMG
                    print(f"You did {mainDMG} to the Mech!")
            if bulletSeed == 4:
                for i in range(4):
                    mainDMG = ((2*50/5 +2) * botATK[6][1] *ATK/ botDEF/50)+2
                    mainDMG = math.floor(mainDMG)
                    totalDMG += mainDMG
                    print(f"You did {mainDMG} to the Mech!")
            if bulletSeed == 5:
                for i in range(5):
                    mainDMG = ((2*50/5 +2) * botATK[6][1] *ATK/ botDEF/50)+2
                    mainDMG = math.floor(mainDMG)
                    totalDMG += mainDMG
                    print(f"You did {mainDMG} to the Mech!")

            return int(totalDMG)

        if botATK[6][0] == 'Weld':
            mainDMG = 0
            return int(mainDMG)

        if botATK[6][0] == 'Sharpen':
           mainDMG = 0
           return int(mainDMG)

    elif moveNum == 1:
        mainDMG = 0
        return int(mainDMG)
                        
    else:
        mainDMG = ((2*50/5 +2) * botATK[5][moveNum][1] *ATK/ botDEF/50)+2
        mainDMG = math.floor(mainDMG)

        return int(mainDMG)

def HP(bot):
    return bot[1]+50+10

def Heal(bot):
    bot.HP = bot.FullHP 

def Weld(bot):
    if (50+bot.HP) > bot.FullHP:
        healed_by = bot.FullHP - bot.HP
        bot.HP += healed_by
        print(f"{bot.name} repaired {healed_by} HP.")
    elif (50+bot.HP) < bot.FullHP:
        bot.HP += 50
        print(f"{bot.name} repaired 50 HP.")

def Iron(bot):
    bot.DEF = bot.DEF * 2
    print(f"{bot.name}'s defense was doubled for 2 turns.")

def EnemyIron(bot):
    bot.DEF = bot.DEF * 2
    print(f"{bot.name}'s defense was doubled for 2 turns.")

def Hone(bot):
    bot.ATK = bot.ATK * 2
    print(f"{bot.name}'s Attack was doubled for 2 turns.")

def EnemyHone(bot):
    bot.ATK = bot.ATK * 2
    print(f"{bot.name}'s Attack was doubled for 2 turns.")
#-----------------------------------Move Sets--------------------------------------

"Move = [Move Name, Power, Accuracy, Power_Points]"

Attack_List = []
Special_List = []

slash = ["Slash", 70, 1.0, 10]
block = ["Block", 10, 1.0, 10]
nail_gun = ["Nail Gun", 90, .75, 10]
iron_fist = ["Iron Fist", 95, .65, 10]

# Sport Unique Move

guillotine = ["Guillotine", 110, .6, 10]  # 0           # Super strong melee attack 

# Tank Unique Move

iron_defense = ["Iron Defense", 10, 10, 10]    # 1       # Halves all enemy attack for 2 turns 1 cool down turn 

# Sniper Unique Move

rivet_gun = ["Rivet Gun", 20, 1.0 , 10]       # 2       # Super strong ranged attack

# Welder Unique Move

weld = ["Weld", 10, 10, 10]          # 3         # Heals player by random amount 

# Battler Unique Move

sharpen = ["Sharpen", 10, 10, 10]     # 4          # doubles attack for 2 turns 1 cool down turn 


Attack_List.append(slash)         #0
Attack_List.append(block)         #1  
Attack_List.append(nail_gun)      #2  
Attack_List.append(iron_fist)     #3  

Special_List.append(guillotine)    #0 
Special_List.append(iron_defense)  #1  
Special_List.append(rivet_gun)     #2
Special_List.append(weld)          #3  
Special_List.append(sharpen)       #4  

#-----------------------------------Bot Selection--------------------------------------

# Speed key: .5 = slow / 1 = regular(broken by a random speed tie)/ 2 = fast
# Melee/Range: .5 = reduced damage/ 1 = regular / 2 = Super Effective 

# bot = Fighter('name', max_hp, melee, range, speed, Attack_List, special)
sport = ['Sport', 70, 130, 65, 2, Attack_List, Special_List[0]]
tank = ['Tank', 140, 80, 100, .5, Attack_List,  Special_List[1]]
sniper = ['Sniper', 100, 110, 80, 1, Attack_List, Special_List[2]]
welder = ['Welder', 100, 100, 70, 1, Attack_List, Special_List[3]]
brawler = ['Brawler', 110, 100, 80, 1, Attack_List, Special_List[4]]

fighterClasses = []
fighterClasses.append(sport)
fighterClasses.append(tank)
fighterClasses.append(sniper)
fighterClasses.append(welder)
fighterClasses.append(brawler)


#-----------------------------------Variables---------------------------------------

PName = ""
player_bot = ""
CurrPokemon = ""
DefPokemon = ""
MoveChoice = ""
CurrHP = ""
DefHP = ""
Damage_Taken = ""
Opponent_MoveChoice = ""

#-----------------------------------Opponent Mechs---------------------------------------
Kershaw = Fighter(brawler)
Gerber = Fighter(sniper)
Buck = Fighter(tank)


#----------------Start and Background---------------------

print(open('logofinal.txt', 'r').read())
print()
PName = input("Welcome to Real Steel! Tell us your name...\n\n")

def background():
    print()
    print("Hello "+PName+", lets get you filled in. Press enter to continue...")
    input()
    print("Year 2235....\n")
    time.sleep(1.5)
    print("The tech company MechaTech is leading in the industry of the most highly popular activity being played around the world since their launch in 2233: Real Steel\n")
    time.sleep(2)
    print("Real Steel is a strategy turn-based activity where participants (known as Steelers) go against each other using their remote controlled robots (known as Mechs) and take turns attacking each other. The first Mech to 0HP, loses.\n")
    time.sleep(2)
    print("Anyone can purchase a Mech and become a Steeler. Mechs come preloaded with classes and movesets tailored to those classes, so Steelers are advised to choose a Mech with a class that fits their playstyle the most.\n")
    time.sleep(2)
    print("The classes are...\n")
    time.sleep(1.5)
    print("Sport: Focuses on close range, has high attack damage, but lowest HP. (Glass Cannon)\n")
    time.sleep(2)
    print("Tank: Close range, low attack damage, but highest HP amongst the classes (Tank)\n")
    time.sleep(2)
    print("Sniper: Long range, medium attack damage, low HP (Archer)\n")
    time.sleep(2)
    print("Welder: Close to medium range, low attack damage, medium HP, ability to heal (Healer)\n")
    time.sleep(2)
    print("and Brawler: Close to medium range, medium attack damage, with medium HP (Well Rounded)\n")
    input("Press enter when ready...\n")
    print("Steelers control their Mechs from the tablet provided to them upon purchasing their Mech. During battle, they can choose from a list of 5 attacks.\n")
    time.sleep(1.5)
    print("Rules are simple:\n")
    time.sleep(1.5)
    print("- Each game you are given 5 lives\n")
    time.sleep(1.5)
    print("- There is a checkpoint at the start of every challenge/battle (Lives reset back to 5)\n")
    time.sleep(1.5)
    print("- Players take turns choosing attacks\n")
    input("Press enter to continue...\n")
  
background()


#----------------Introduction---------------------

def intro():
    print("Present day, Year 2236…\n")
    time.sleep(2)
    print(PName,"holds one of the records for the best win/loss ratio in his town: 50-5\n")
    time.sleep(1.5)
    print("MechaTech has announced for their third anniversary that they have gathered three of the best Steelers called the “Alloys.”\n")
    time.sleep(1.5)
    print("MechaTech is giving anyone the chance to face the Alloys, but competing Steelers must complete a small challenge presented to them prior to facing each of the Alloys.\n")
    time.sleep(1.5)
    print("The Steeler that defeats all three Alloys will become the world's best known as the “Stainless”, a title just announced by MechaTech that stands above the Alloys and is currently vacant. The winner will hold that title until someone defeats them along with the Alloys.\n")
    input("Press enter to continue...\n")
    
intro()


#------------------Riddle------------------
def riddle():
    print(PName,"has grown bored of winning against the same people in their town and was itching for a real challenge.\n")
    time.sleep(1.5)
    print ("They took interest in the competition when it was announced and immediately went online to sign up for the chance to become the Stainless.\n")
    time.sleep(1.5)
    print("When they opened the website to the application, the website displayed a message...\n" )
    time.sleep(1.5)
    print("The message read,\n")
    time.sleep(1.5)
    print("A STRONG STEELER MUST EXERCISE HIS THINKING BOTH IN AND OUT OF BATTLE. IN ORDER TO GAIN ACCESS TO THE APPLICATION TO FACE THE ALLOYS, YOU MUST CORRECTLY SOLVE THIS RIDDLE.\n")
    input("Press enter to begin solving the riddle.\n")
riddle()


def riddles():
        randrid = random.randint(1,8)
        gameend = '''
        
         ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
        ██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
        ██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
        ██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
         ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██ 
       
         '''                                                                         
    
        while randrid == 1:
            answer = 'egg'
            hint1 = 'I am a popular breakfast choice\n'
            hint2 = 'Chicken\n'
            riddle = input("---What has to be broken before you can use it?---\nType your guess, or type 'hint1', hint2', or 'I give up' below.\n")
            
            if answer in riddle.lower():
                print ("\nThat is correct!")
                time.sleep(1.5)
                print("The answer is: " + answer)
                break
            
            elif riddle.lower() == 'hint1' or riddle.lower() == 'hint 1':
                    print("\nHint: " + hint1)
                    
                    
            elif riddle.lower() == 'hint2' or riddle.lower() == 'hint 2':
                    print("\nHint: " + hint2)
                    
                
            elif riddle.lower() == 'i give up':
                print("The answer was: " + answer)
                print(gameend)
                exit()
            
            else:
                print ("\nThat is incorrect. Try again!")
            continue
                
    
    
    
        while randrid == 2:
            answer = 'sponge'
            hint1 = 'I am used for washing dishes\n'
            hint2 = 'Popular Cartoon\n'
            riddle = input("---What is full of holes but still holds water?---\nType your guess, or type 'hint1', hint2', or 'I give up' below.\n")
            
            if answer in riddle.lower():
                print ("\nThat is correct!")
                time.sleep(1.5)
                print("The answer is: " + answer)
                break
            
            elif riddle.lower() == 'hint1' or riddle.lower() == 'hint 1':
                    print("\nHint: " + hint1)
                    
                    
                    
            elif riddle.lower() == 'hint2' or riddle.lower() == 'hint 2':
                    print("\nHint: " + hint2)
                    
                
            elif riddle.lower() == 'i give up':
                print("The answer was: " + answer)
                print(gameend)
                exit()
            
            else:
                print ("\nThat is incorrect. Try again!")
            continue    
            
    
        while randrid == 3:
            answer = 'towel'
            hint1 = 'You probably take me to the beach\n'
            hint2 = 'You use me after a shower\n'
            riddle = input("---What gets wet while drying?---\nType your guess, or type 'hint1', hint2', or 'I give up' below.\n")
            
            if answer in riddle.lower():
                print ("\nThat is correct!")
                time.sleep(1.5)
                print("The answer is: " + answer)
                break
            
            elif riddle.lower() == 'hint1' or riddle.lower() == 'hint 1':
                    print("\nHint: " + hint1)
                    
                    
            elif riddle.lower() == 'hint2' or riddle.lower() == 'hint 2':
                    print("\nHint: " + hint2)
                    
                
            elif riddle.lower() == 'i give up':
                print("The answer was: " + answer)
                print(gameend)
                exit()
            
            else:
                print ("\nThat is incorrect. Try again!")              
            continue    
            


        while randrid == 4:
            answer = 'piano'
            hint1 = 'I am an instrument\n'
            hint2 = 'Beethoven used me for his music\n'
            riddle = input("---What has many keys but can't open a single lock?---\nType your guess, or type 'hint1', hint2', or 'I give up' below.\n")
            
            if answer in riddle.lower():
                print ("\nThat is correct!")
                time.sleep(1.5)
                print("The answer is: " + answer)
                break
            
            elif riddle.lower() == 'hint1' or riddle.lower() == 'hint 1':
                    print("\nHint: " + hint1)
                    
                    
            elif riddle.lower() == 'hint2' or riddle.lower() == 'hint 2':
                    print("\nHint: " + hint2)
                    
                
            elif riddle.lower() == 'i give up':
                print("The answer was: " + answer)
                print(gameend)
                exit()
            
            else:
                print ("\nThat is incorrect. Try again!")              
            continue    
                


        while randrid == 5:
            answer = 'tongue'
            hint1 = "I'm the reason you're able to speak\n"
            hint2 = 'Body part\n'
            riddle = input("---What taste better than it smells?---\nType your guess, or type 'hint1', hint2', or 'I give up' below.\n")
            
            if answer in riddle.lower():
                print ("\nThat is correct!")
                time.sleep(1.5)
                print("The answer is: " + answer)
                break
            
            elif riddle.lower() == 'hint1' or riddle.lower() == 'hint 1':
                    print("\nHint: " + hint1)
                    
                    
            elif riddle.lower() == 'hint2' or riddle.lower() == 'hint 2':
                    print("\nHint: " + hint2)
                    
                
            elif riddle.lower() == 'i give up':
                print("The answer was: " + answer)
                print(gameend)
                exit()
            
            else:
                print ("\nThat is incorrect. Try again!")              
            continue
                
  
    
        while randrid == 6:
            answer = 'library'
            hint1 = "I'm really quiet\n"
            hint2 = 'People go here to research and do homework\n'
            riddle = input("---What building has the most stories?---\nType your guess, or type 'hint1', hint2', or 'I give up' below.\n")
            
            if answer in riddle.lower():
                print ("\nThat is correct!")
                time.sleep(1.5)
                print("The answer is: " + answer)
                break
            
            elif riddle.lower() == 'hint1' or riddle.lower() == 'hint 1':
                    print("\nHint: " + hint1)
                    
                    
            elif riddle.lower() == 'hint2' or riddle.lower() == 'hint 2':
                    print("\nHint: " + hint2)
                    
                
            elif riddle.lower() == 'i give up':
                print("The answer was: " + answer)
                print(gameend)
                exit()
            
            else:
                print ("\nThat is incorrect. Try again!")              
            continue    
                   
    
 
        while randrid == 7:
            answer = 'david'
            hint1 = 'His name is already mentioned\n'
            hint2 = 'Star of _____\n'
            riddle = input("---David’s parents have three sons: Snap, Crackle, and what’s the name of the third son?---\nType your guess, or type 'hint1', hint2', or 'I give up' below.\n")
            
            if answer in riddle.lower():
                print ("\nThat is correct!")
                time.sleep(1.5)
                print("The answer is: " + answer)
                break
            
            elif riddle.lower() == 'hint1' or riddle.lower() == 'hint 1':
                    print("\nHint: " + hint1)
                    
                    
            elif riddle.lower() == 'hint2' or riddle.lower() == 'hint 2':
                    print("\nHint: " + hint2)
                    
                
            elif riddle.lower() == 'i give up':
                print("The answer was: " + answer)
                print(gameend)
                exit()
            
            else:
                print ("\nThat is incorrect. Try again!")              
            continue    
                
    
    
        while randrid == 8:
            answer = 'candle'
            hint1 = 'I give light.\n'
            hint2 = "I'm made of wax.\n"
            riddle = input("---I’m tall when I’m young and I’m short when I’m old. What am I?---\nType your guess, or type 'hint1', hint2', or 'I give up' below.\n")
            
            if answer in riddle.lower():
                print ("\nThat is correct!")
                time.sleep(1.5)
                print("The answer is: " + answer)
                break
            
            elif riddle.lower() == 'hint1' or riddle.lower() == 'hint 1':
                    print("\nHint: " + hint1)
                    
                    
            elif riddle.lower() == 'hint2' or riddle.lower() == 'hint 2':
                    print("\nHint: " + hint2)
                    
                
            elif riddle.lower() == 'i give up':
                print("The answer was: " + answer)
                print(gameend)
                exit()
            
            else:
                print ("\nThat is incorrect. Try again!")              
            continue            
        
riddles()

    
#---------------First Puzzle---------------    
    
def firstpuzzle():
    input("Press enter to continue.\n")
    print("After solving the riddle,",PName,"was directed to the application and filled it out.\n")
    time.sleep(1.5)
    print("Your journey to end your boredom and become the world's best has now begun!\n")
    time.sleep(3)
    print("One week later...\n")
    time.sleep(2)
    print(PName,"booked a flight to San Francisco where MechaTech Stadium is located.\n")
    time.sleep(1.5)
    print("After checking into his hotel and spending the night, they woke up early the next morning and took a Goober to the Stadium.\n")
    time.sleep(1.5)
    print("Outside of it are hundreds of Steelers eager for their opportunity to face the Alloys.\n")
    time.sleep
    print("As",PName,"is waiting in line and is slowly approaching the door to the first Alloy, they constantly see the same people that entered before them come back out and exit the stadium with frowns upon their faces.\n")
    time.sleep(2)
    print("When trying to take a peak at whats beyond the door that's not far now, they notice Steelers are entering the door in pairs. The room was a bit too dark to see what was inside it.\n")
    time.sleep(2)
    print("After waiting for three hours,",PName,"enters the door along with the Steeler in from of them.\n")
    time.sleep(1.5)
    print("The room is dimly lit and as soon as the door closes, the lights turn on.\n")
    time.sleep(1.5)
    print("In front of them is a MechaTech worker standing in front of another large door that possibly leads to the arena to face the first Alloy.\n")
    time.sleep(1.5)
    print("The MechaTech worker tells the Steelers that they are to play a simple game of Rock, Paper, Scissors. Best 2 out of 3 wins. Whoever loses will immediately be disqualified and asked to leave the stadium!\n")
    time.sleep(2)
    print("The Steelers face each other and are instructed to begin when ready.")
    input("Press enter to begin!")   
firstpuzzle()    



def rps():
    winning=2
    #scores
    comp=0
    p=0
    #scores


    while p<winning and comp<winning: 
    	rand_num = randint(0,2)
    	print("Opponent score:",comp, PName,"score:",p,"\n")
    	player = input("Make your move: Rock, Paper, or Scissors? or Quit? \n").lower()
    	if player=="quit" or player=="q":
                print("""
                                   
     ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
    ██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
    ██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
    ██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
     ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██ 
                                                                             
            """)
                exit()
    	if rand_num == 0:
    		computer = "rock"
    
    	elif rand_num == 1:
    		computer = "paper"
    
    	else:
    		computer = "scissors"
    
    	print(f"Opponent plays {computer} \n" )
    
    	if player == computer:
    		print("It's a tie!\n")
    
    	elif player == "rock":
    		if computer == "scissors":
    			print(PName,"wins this round!\n")
    			p+=1
    		else:
    			print("Opponent wins this round!\n")
    			comp+=1
    	elif player == "paper":
    		if computer == "rock":
    			print(PName,"wins this round!\n")
    			p+=1
    		else:
    			print("Opponent wins this round!\n")
    			comp+=1
    	elif player == "scissors":
    		if computer == "paper":
    			print(PName,"wins!\n")
    			p+=1
    		else:
    			print("Opponent wins this round!\n")
    			comp+=1
    	else:
    			print("Please enter a valid move!\n")
    while comp>p:
        gamecont = input("Opponent wins the match. You lose. Would you like to continue? Y/N \n").lower()
        if gamecont=="yes" or gamecont=="y":
            rps()
            break
        elif gamecont=="no" or gamecont=="n":
            print("You are asked to exit the premises.")
            print("""
                                                     
         ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
        ██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
        ██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
        ██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
         ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██ 
        
                  """)
            exit()
        else:
            print("That is not a valid response.")
            continue
    if p>comp:
        print(PName,"wins the match!")
        time.sleep(2)
        input("Press enter to continue...")

rps()



#------------------First Battle------------------
print()
print (f"After successfully winning, it is now time for {PName} to choose their Mech.\n")
time.sleep(1.5)
print("Who will you choose?\n")
time.sleep(1.5)
print(("*") * 40)
print()
print("Sport, the the Glass Cannon Mech.")
print("- Special Move: Guillotine- Very high attack damage (60% Accuracy)\n")
time.sleep(1.5)
print("Tank, the the Defensive Mech.")
print("- Special Move: Iron Defense- Defense Stat is doubled for 2 turns\n")
time.sleep(1.5)
print("Sniper, the the Ranged Mech.")
print("- Special Move: Rivet Gun- Attack can hit 2-5 times\n")
time.sleep(1.5)
print("Welder, the the Repairng Mech.")
print("- Special Move: Weld- Repairs 50 HP\n")
time.sleep(1.5)
print("Brawler, the the Well Rounded Mech.")
print("- Special Move: Sharpen- Attack is doubled for 2 turns\n")
time.sleep(1.5)
print(("*") * 40)

StarterMech = input("Mech choice: ")
StarterMech = StarterMech.upper()
GoodStarter = False

while not GoodStarter:
    if StarterMech == "SPORT":
        player_bot = Fighter(sport)
        GoodStarter = True
    elif StarterMech == "TANK":
        player_bot = Fighter(tank)
        GoodStarter = True
    elif StarterMech == "SNIPER":
        player_bot = Fighter(sniper)
        GoodStarter = True
    elif StarterMech == "WELDER":
        player_bot = Fighter(welder)
        GoodStarter = True
    elif StarterMech == "BRAWLER":
        player_bot = Fighter(brawler)
        GoodStarter = True
    else:
        print("Sorry but that Mech is unavailable.")
        print("Pick your choice again.")
        StarterMech = input("Mech choice: ")
        StarterMech = StarterMech.upper()
        
  



def firstbattle():
    print ("Now that ",PName," has chosen his Mech, he gives his oppenent best of wishes then walks through the door and sees the arena. They approach it and wait...\n")
    time.sleep(1.5)
    print ("The door on the opposite end of the arena opens and the first Alloy walks up and presents himself as “Kershaw”\n")
    time.sleep(1.5)
    print("Upon glancing at Kershaw’s Mech,",PName,"notices Kershaw owns a Mech that is a Brawler class.\n")
    time.sleep(1.5)
    print("Kershaw continues to introduce himself and states his record is 70-4!\n")
    time.sleep(1.5)
    print("He then sends his Mech to the field...\n")
    time.sleep(1.5)
    print (PName,"sends their Mech...\n")
    input("Press enter to begin battle...\n")
    print("The battle begins!\n")
firstbattle()  
battle("Kershaw", Kershaw)




#----------------Second Puzzle--------------------

def secondpuzzle():
    print("Kershaw commends",PName)
    time.sleep(1.5)
    print("He allows",PName,"to proceed for his next challenge.\n")
    time.sleep(1.5)
    print("They approach the door and enter a small square room with one other door.\n")
    time.sleep(1.5)
    print("After entering the room, the door behind them slams shut!\n")
    time.sleep(1.5)
    print(PName,"rushes to the door in front of them and finds out it's locked!\n")
    time.sleep(1.5)
    print("An intercom turns on and begins to tell",PName,"that it’s time for the next challenge; Hangman!\n")
    time.sleep(1.5)
    print("If the player loses, the floor will open up like a gallow, they will fall all the way down, and lose the competition.\n")
    time.sleep(1.5)
    print("The game projects onto the wall...\n")
    time.sleep(1.5)
    input("Press enter to begin Hangman\n")
secondpuzzle()

metals = ['gold', 'silver', 'titanium', 'copper', 'platinum', 'iron','nickel', 'lead','tungsten','cobalt']
mechanics = ['gear', 'sprocket', 'radiator', 'condenser', 'engine', 'alternator', 'pump', 'compressor', 'battery', 'wire']

def get_word(word_list):
    word= random.choice(word_list)
    return word.upper()

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]



guessed = False
guessed_letters = []
guessed_words = []
tries = 6 
play_game = True

while play_game == True:
    
    category = input("Please select a valid category: M for Metals / P for Mechanical Parts.\n").upper()
    valid_category = False
    while not valid_category:
        if category == "M":
            word = get_word(metals)
            valid_category= True
        elif category == "P":
            word = get_word(mechanics)
            valid_category= True
        else:
            print("Sorry I coulnd't understand you.")
            category = input("Please select a valid categary: M for Metals / P for Mechanical Parts; X to exit\n").upper()
            
    word_completion = "_" * len(word)
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    
    while not guessed and tries > 0 :
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word: 
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True 
                word_completion = word
        else:
            print("Not a valid guess.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("You guessed it right! You Won!")
        play_game = False
        
    else:
        print(f"Sorry, you ran out of tries. The word was {word}.")
        print()
        time.sleep(1.5)
        print("The floor suddenly opens!",PName,"falls all the way down and lands in a large pit filled with blocks of sponges!\n")
        time.sleep(1.5)
        print("They’re approached by a worker of MechaTech and informs them that they have lost and gets escorted out the Stadium...\n")
        play_again = input("Would you like to play again? (Y/N): ").upper()
        good_choice = False
        while not good_choice:
            if play_again == "Y":
                guessed = False
                tries = 6
                guessed_letters = []
                guessed_words = []
                good_choice =True
            elif play_again =="N":
                print("""
                                   
     ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
    ██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
    ██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
    ██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
     ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██ 
                   """)
                exit()
                good_choice =True
            else:
                print("Sorry I coulnd't understand you.")
                play_again = input("Would you like to play again? (Y/N): ").upper()
            




#----------------Second Battle--------------------

def secondbattle():
    print("Both doors in the room unlocked.\n")
    time.sleep(2)
    print(PName,"proceeds forward.\n")
    print ("They see the next arena and approach it...\n")
    time.sleep(1.5)
    print ("The large door on the opposite side opens and the next Alloy walks through it.\n")
    time.sleep(1.5)
    print("He introduces himself as Gerber and mentions the class of his mech is a Sniper.\n")
    time.sleep(1.5)
    print(PName,"introduces themself and Gerber wishes best of luck.\n")
    time.sleep(1.5)
    print("Both Mechs are sent to the arena...\n")
    input("Press enter to begin battle...\n")
    print("The battle begins!\n")
    time.sleep(1.5)
    

    
secondbattle()
battle("Gerber", Gerber)



#----------------Third Puzzle/Battle--------------------

def thirdbattleandpuzzle():
    print("Gerber commends and thanks the player for a great match and gives permission to proceed.\n")
    time.sleep(1.5)
    print (PName,"approaches what seems to be the largest door in the Stadium....\n")
    time.sleep(1.5)
    print ("The door opens and",PName,"is immediately greeted with the arena and the final Alloy standing at the opposite end.\n")
    time.sleep(1.5)
    print("The Alloy says he goes by the name “Buck.”\n")
    time.sleep(1.5)
    print("He mentions that he is the best out of the three Alloys with a record of 100-2!\n")
    time.sleep(1.5)
    print("His Mech's class is a Tank.\n")
    time.sleep(1.5)
    print (PName,"asks why he isn’t solving a puzzle.\n")
    time.sleep(1.5)
    print ("Buck says this match will be the hardest, so a simple coin toss is the only thing needed to get the battle started.\n")
    time.sleep(1.5)
    print("A game of luck stands in your way to become the Stainless!\n")
    input("Press enter to begin coin toss...\n")
thirdbattleandpuzzle()



def flipcoin():
    a = ["Heads" , "Tails"]
    computer = a[randint(0,1)]
    return computer

def cointoss():
    print("Heads or Tails game started. Best 2 out of 3 wins.")
    score = 0
    op_score = 0
    n = int(3)
    b = n
    while n>0:
        user_guess = input("Heads or Tails:\n").lower()
        if user_guess == "heads" or user_guess == "tails":
            coin = flipcoin()
            if coin.lower() == user_guess:
                print("Good guess!")
                score = score + 1
            elif coin.lower() != user_guess:
              print("Wrong")
              op_score = op_score + 1
            else:
                print("You lost that round!")
        else:
            print("Not a valid choice! Write either Heads or Tails")
            n = n+1
        n = n-1
    
        if score == 2:
            print("Your score:" ,score, "out of" ,b)
            input("You win! Press enter to begin battle!\n")
            battle("Buck", Buck)
            break
        
    
        while op_score == 2:
          print("\nBuck's score:" ,op_score, "out of" ,b,"You lost.\n")
          gamecont = input("Try again? Y/N\n")
          if gamecont=="y" or gamecont=="yes":
              cointoss()          
          elif gamecont=="n" or gamecont=="no":
              print("You were asked to leave the premises.\n")
              print("""
                          
    ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
   ██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
   ██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
   ██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
    ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██ 
                                                                            
                          """)
              exit()
              break
          else:
              print("That is not a valid option.\n")
              continue
              
cointoss()



def outro():
    print ("Buck walks up to",PName,"to shake his hand and congratulate them.\n")
    time.sleep(1.5)
    print ("They both walked outside to where all other contestants were and they all started applauding. Even Kershaw and Gerber were amongst the crowd.\n")
    time.sleep(2)
    print("Buck tells",PName,"he now holds the top title and will have many people attempting to take it.\n")
    time.sleep(1.5)
    print("Buck gives them a badge for proof of the title.\n")
    time.sleep(1.5)
    print("They once again turn to the crowd and Buck says…\n")
    time.sleep(1.5)
    print (PName,"must now fight all of the contestants that manage to best the Alloys!\n")
    time.sleep(1.5)
    print("You have completed your goal on ending you boredom and becoming the world's best, but another journey begins: You must now defend your title!")
    time.sleep(3)
    print ("To be continued...\n")
    time.sleep(2)
    input("Congratulations! You win! Press enter to end game.\n")
    print("""         
 

 /$$$$$$$$ /$$   /$$  /$$$$$$  /$$   /$$ /$$   /$$       /$$     /$$ /$$$$$$  /$$   /$$       /$$$$$$$$ /$$$$$$  /$$$$$$$        /$$$$$$$  /$$        /$$$$$$  /$$     /$$ /$$$$$$ /$$   /$$  /$$$$$$ 
|__  $$__/| $$  | $$ /$$__  $$| $$$ | $$| $$  /$$/      |  $$   /$$//$$__  $$| $$  | $$      | $$_____//$$__  $$| $$__  $$      | $$__  $$| $$       /$$__  $$|  $$   /$$/|_  $$_/| $$$ | $$ /$$__  $$
   | $$   | $$  | $$| $$  \ $$| $$$$| $$| $$ /$$/        \  $$ /$$/| $$  \ $$| $$  | $$      | $$     | $$  \ $$| $$  \ $$      | $$  \ $$| $$      | $$  \ $$ \  $$ /$$/   | $$  | $$$$| $$| $$  \__/
   | $$   | $$$$$$$$| $$$$$$$$| $$ $$ $$| $$$$$/          \  $$$$/ | $$  | $$| $$  | $$      | $$$$$  | $$  | $$| $$$$$$$/      | $$$$$$$/| $$      | $$$$$$$$  \  $$$$/    | $$  | $$ $$ $$| $$ /$$$$
   | $$   | $$__  $$| $$__  $$| $$  $$$$| $$  $$           \  $$/  | $$  | $$| $$  | $$      | $$__/  | $$  | $$| $$__  $$      | $$____/ | $$      | $$__  $$   \  $$/     | $$  | $$  $$$$| $$|_  $$
   | $$   | $$  | $$| $$  | $$| $$\  $$$| $$\  $$           | $$   | $$  | $$| $$  | $$      | $$     | $$  | $$| $$  \ $$      | $$      | $$      | $$  | $$    | $$      | $$  | $$\  $$$| $$  \ $$
   | $$   | $$  | $$| $$  | $$| $$ \  $$| $$ \  $$          | $$   |  $$$$$$/|  $$$$$$/      | $$     |  $$$$$$/| $$  | $$      | $$      | $$$$$$$$| $$  | $$    | $$     /$$$$$$| $$ \  $$|  $$$$$$/
   |__/   |__/  |__/|__/  |__/|__/  \__/|__/  \__/          |__/    \______/  \______/       |__/      \______/ |__/  |__/      |__/      |________/|__/  |__/    |__/    |______/|__/  \__/ \______/ 
                                                                                                                                                                                                      
                                                                                                                                                                                                      
                                                                                                                                                                                                      

                                                                                                 
          """)

outro()
    
    
    
    
    
    
    