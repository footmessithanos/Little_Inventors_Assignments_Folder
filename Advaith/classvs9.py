import time
print("Welcome to my amazing game (Not like Advaith.Basireddy's)")
print("This game is about story telling")
d = input("What's your name  ")
j = input("What do you want to name your charecter   ")
print("Choose your weponry,", d)
print("1. No weapon")
print("2. Daggers")
print("3. Bow")
print("4. Sword")
print("5. Gun")
a = int(input("Choose your bloody weapon  "))
try:
    print("Ok. %d is chosen " %(a))
    print("Which shield do you choose")
    b = int(input("1 = metal, 2 = wooden, 3 = no shield.  "))
    if b ==1:
        print("Ok, it is %s" %('metal'))
    elif b == 2:
        print("Ok, it is wooden")
    else:
        print("Ok, no weapon")
    if b != 3:
        print("1. Square shaped")
        print("2. Diamond shaped")
        print("3. Rectangluar shaped")
        print("4. Ovalar shaped")
        c = int(input("What do you want to choose  "))
        print("Ok. %d is chosen" %(c))
    print("Now the story BEGINS!")
    print("You were born in an alien planet and you were sent to Earth at the age 2")
    print("You had super powers before")
    print("But your arch enemy took them all. But he couldn't kill you")
    print("Because you were too strong")
    print("Now, he wants to rule Earth")
    print("The world depends on you,", j)
    print("No one should speak 'his' name. We call him 'human-evil'")
    print("Human-evil's name is Ad-A-Adv-Advaith.Basireddy")
    print("If you speak human-evils name 5 times you you will be cursed")
    time.sleep(5)
    print("Oh no human-evils minion's minion is coming. Tata bye-bye!")
    print("1 = Call your best friend as back up(he will come in 1 min)")
    print("2 = Fight with her")
    print("3 = Run away")
    print("4 = Call your company as back up(2 min & 10 persons)")
    print("5 = Let her kill you")
    print("6 = Tell human-evil's name 5 times")
    e = int(input("What do you choose  "))
    if e == 1:
        print("Oh no she's asking you to fight with her")
        print("1 = Fight with her")
        print("2 = Run away")
        print("3 = Let her kill you")
        f = int(input("What do you do  "))
        if f == 1:
            print("Ok. Fight")
            time.sleep(5)
            print("Now you win and back up comes and arrests her")
        elif f == 2:
            print("Now you run of far and you see your back up")
            print("1.= Go with him and fight her")
            print("2.= Ask him to run with you")
            print("3.= Ask him only to fight her")
            g = int(input("What do you do  "))
            if g == 1:
                print("Ok. Fighting")
                time.sleep(2)
                print("Now your best friend dies")
                print("1 Run away")
                print("2 Keep fighting")
                h = int(input("Choose one  "))
                if h == 1:
                    print("Now you see a 'HUMAN-EVIL'!")
                    print("He kills you")
                    print("Thanks for playing this", d)
                    print("This is the end of version 1.0")
                    exit("Tata bye-bye")
                elif h == 2:
                    print("Ok. Fighting")
                    time.sleep(5)
                    print("You win!")
                else:
                    print("Try again!")
                    exit()
            elif g == 2:
                print("Now you see a 'HUMAN-EVIL'!")
                print("He kills you and her")
                print("Thanks for playing this", d)
                print("This is the end of version 1.0")
                exit("Tata bye-bye")
            else:
                print("He says,'Ok, you stay here.'")
                print("And he goes to fight her")
                print("Now you see a 'HUMAN-EVIL'!")
                print("He kills you")
                print("Thanks for playing this", d)
                print("This is the end of version 1.0")
                exit("Tata bye-bye")
        else:
            print("Now you are stabbed and in 5 seconds you'll be killed")
            time.sleep(5)
            print("Now your best friend comes and sees this and kills her")
            print("He takes you to the hospital")
            print("The doctors say that because you are not from Earth they don't know your organs")
            print("Now you see a 'HUMAN-EVIL'!")
            print("He kills you")
            print("Thanks for playing this", d)
            print("This is the end of version 1.0")
            exit("Tata bye-bye")
    elif e == 2:
        print("Ok. Fighting")
        time.sleep(2)
        print("She stabs your leg and gets a shock cause you are an alien")
        print("Now she's down for a few mins")
        print("1 = Call your friend as back up(2 min)")
        print("2 = Call your company as back up(4 min)")
        print("3 = Let her wake up and kill you(5 min)")
        i = int(input("Which one  "))
        if i == 1:
            print("You pick your phone and call him")
            print("He tells,'Ok I'll reach there in 2 min, google maps'.")
            time.sleep(2)
            print("Now, human-evil sees him")
            print("He fights hi, but he looses. Then human-evil kills him")
            print("Now, she gets up from her shock and shots you")
            print("Now you are dead")
            print("Thanks for playing this", d)
            print("This is the end of version 1.0")
            exit("Tata bye-bye")
        elif i == 2:
            print("You pick your phone and call them")
            print("They tell,'Ok I'll reach there in 4 min, google maps'.")
            time.sleep(4)
            print("Now, human-evil sees them")
            print("Now, they fight against them")
            print("Then they stab human-evil's knee")
            print("Human-evil fell and your company is running to you")
            print("Now, they have arrived to save you")
            print("Now, she gets up from the shock")
            print("Now Your crew kills her")
        else:
            time.sleep(5)
            print("Now she kills you")
            print("Thanks for playing this", d)
            exit()
    elif e == 3:
        print("Ok. Running")
        print("You will take 5 sec to run away")
        time.sleep(5)
        print("Now your arch enemie is in front ")
        print("What do you do")
        print("1. Fight him")
        print("2. Run back and fight his minion")
        print("3. Call for help(2 min)")
        print("4. Die on spot")
        k = int(input("Which one do you choose  "))
        if k == 1:
            print("Ok fighting")
            time.sleep(5)
            print("Oh! You died")
            print("I forgot to warn you, he is stronger")
            print("Thanks for playing this", d)
            exit("Tata, bye-bye")
        elif k==2:
            print("Ok. Running back")
            time.sleep(2)
            print("I forgot to warn you, he is faster")
            print("He has caught you and killed you")
            print("Thanks for playing this", d)
            exit("Tata, bye-bye")
        elif k==3:
            print("Ok. You pick your phone and call help")
            print("But human-evil kills you before they come")
            print("Thanks for playing this", d)
            exit("Tata, bye-bye")
        else:
            print("Ok. Dying")
            print("Thanks for playing this", d)
            exit("Tata, bye-bye")
    elif e == 4:
        print("Oh no she's asking you to fight with her")
        print("1 = Fight with her")
        print("2 = Run away")
        print("3 = Let her kill you")
        f = int(input("What do you do  "))
        if f == 1:
            print("Ok. Fight")
            time.sleep(5)
            print("Now you win and back up comes and arrests her")
        elif f == 2:
            print("Now you run of far and you see your back up")
            print("1.= Go with him and fight her")
            print("2.= Ask him to run with you")
            print("3.= Ask him only to fight her")
            g = int(input("What do you do  "))
            if g == 1:
                print("Ok. Fighting")
                time.sleep(2)
                print("Now your best friend dies")
                print("1 Run away")
                print("2 Keep fighting")
                h = int(input("Choose one  "))
                if h == 1:
                    print("Now you see a 'HUMAN-EVIL'!")
                    print("He kills you")
                    print("Thanks for playing this", d)
                    print("This is the end of version 1.0")
                    exit("Tata bye-bye")
                elif h == 2:
                    print("Ok. Fighting")
                    time.sleep(5)
                    print("You win!")
                else:
                    print("Try again!")
                    exit()
            elif g == 2:
                print("Now you see a 'HUMAN-EVIL'!")
                print("He kills you and her")
                print("Thanks for playing this", d)
                print("This is the end of version 1.0")
                exit("Tata bye-bye")
            else:
                print("He says,'Ok, you stay here.'")
                print("And he goes to fight her")
                print("Now you see a 'HUMAN-EVIL'!")
                print("He kills you")
                print("Thanks for playing this", d)
                print("This is the end of version 1.0")
                exit("Tata bye-bye")
        else:
            print("Now you are stabbed and in 5 seconds you'll be killed")
            time.sleep(5)
            print("Now your best friend comes and sees this and kills her")
            print("He takes you to the hospital")
            print("The doctors say that because you are not from Earth they don't know your organs")
            print("Now you see a 'HUMAN-EVIL'!")
            print("He kills you")
            print("Thanks for playing this", d)
            print("This is the end of version 1.0")
            exit("Tata bye-bye")
    elif e == 5:
        print("Ok. Killing")
        time.sleep(2)
        print("Thanks for playing this game", d)
        exit("Tata, bye-bye")
    elif e == 6:
        print("Ok telling")
        time.sleep(2)
        print("Now human-evil's minion's minion informed human-evil and he comes")
        print("1. Run away")
        print("2. Fight with him")
        print("3. Die on spot")
        k = int(input("Which one  "))
        if k == 1:
            print("Ok. Running")
            time.sleep(2)
            print("Because you are unlucky you trip on a stone and fall")
            print("Now human-evil catches you and kills you")
            print("Thanks for playing %s/%s" %(d, j))
            exit("Tata, bye-bye")
        elif k == 2:
            print("Ok, fighting")
            time.sleep(2)
            print("Because you are unlucky he kills you")
            print("Thanks for playing %s/%s" %(d, j))
            exit("Tata, bye-bye")
        else:
            print("Ok, killing")
            time.sleep(5)
            print("Thanks for playing %s/%s" %(d, j))
            exit("Tata, bye-bye")
    else:
        print("Sorry cant help with that")
except Exception as w:
    print("Sorry can't help")
    print("Thanks for playing this game", d)
    exit("Tata, bye-bye")
print("Congrats!")
print("Now you go to a training school")
print("There are 2 trained professionals, pick one to coach you")
print("1 = Kris = swords(attack and defence)")
print("2 = Bablu = shield(attack and defence)")
l = int(input("Pick a coach for you "))
if l == 1:
    n = '____________'
    print("Ok training")
    print("He'll train in 12 days(in our world 12 seconds)")
    time.sleep(1)
    n = list(n)
    for m in range(0, 12):
        print(n)
        time.sleep(1)
        n[m] = '-'
    "".join(n)
    print("Done training")
    print("You know-;")
    print("sword shield, sword block, sword clash, cut arrow, sword throw, sword jump and sword slash")
    print("Oh no :[")
    print("A minion of human-evil found out that you were in this school")
    print("He's coming your way")
    print("1 - run far away")
    print("2 - stay and fight")
    print("3 - Tell human-evils name 5 times")
    o = int(input("What is your decision"))
    if o == 1:
        print("Ok. Running")
        print("You will jump out of the window and jump")
        time.sleep(5)
        print("Ohhh! No, human-evil is in front of you")
        print("1 <fight him>")
        print("2 <run away>")
        print("3 <die>")
        p = int(input("What do you do   "))
        if p == 1:
            print("Ok fighting")
            time.sleep(2)
            print("He kills you")
            print("Thanks for playing this %s or %s" %(d, j))
            exit("Tata, bye-bye")
        elif p==1:
            print("Ok running")
            time.sleep(2)
            print("He is faster than you")
            print("He catches you and kills you")
            print("Thanks for playing this %s or %s" %(d, j))
            exit("Tata, bye-bye")
        else:
            print("Ok dying")
            time.sleep(2)
            print("He kills you")
            print("Thanks for playing this %s or %s" %(d, j))
            exit("Tata, bye-bye")
    elif o == 2:
        print("Ok staying")
        time.sleep(8)
        print("Now his minion comes and fights with all of you")
        time.sleep(2)
        print("He injures you and dies because Rishik kills him")
        print("They take you to a hospital")
        print("The doctors say that you can't recover")
        print("Because you are an alien")
        print("Now you die")
        print("Thanks for playing this %s or %s" %(d, j))
        exit("Tata, bye-bye")
    else:
        print("Ok telling")
        time.sleep(2)
        print("told")
        print("Now theres an Earthquake and you die in it")
        print("Thanks for playing %s or %s" %(d, j))
        exit("Tata, bye-bye")
elif l == 2:
    q = '____________'
    print("Ok training")
    print("He'll train in 12 days(in our world 12 seconds)")
    time.sleep(1)
    for r in range(0, 12):
        print(q, end = "/r")
        time.sleep(1)
        q = list(q)
        q[r] = '-'
        "".join(q)
    print("Done training")
    print("You know-;")
    print("sword shield, shield block, shield strike, cut arrow, shield throw, shield jump and shield slash")
    print("Oh no :[")
    print("A minion of human-evil found out that you were in this school")
    print("He's coming your way")
    print("1 - run far away")
    print("2 - stay and fight")
    print("3 - Tell human-evils name 5 times")
    s = int(input("What is your decision"))
    if s == 1:
        print("Ok. Running")
        print("You will jump out of the window and jump")
        time.sleep(5)
        print("Ohhh! No, human-evil is in front of you")
        print("1 <fight him>")
        print("2 <run away>")
        print("3 <die>")
        p = int(input("What do you do   "))
        if p == 1:
            print("Ok fighting")
            time.sleep(2)
            print("He kills you")
            print("Thanks for playing this %s or %s" %(d, j))
            exit("Tata, bye-bye")
        elif p==1:
            print("Ok running")
            time.sleep(2)
            print("He is faster than you")
            print("He catches you and kills you")
            print("Thanks for playing this %s or %s" %(d, j))
            exit("Tata, bye-bye")
        else:
            print("Ok dying")
            time.sleep(2)
            print("He kills you")
            print("Thanks for playing this %s or %s" %(d, j))
            exit("Tata, bye-bye")
    elif s == 2:
        print("Ok staying")
        time.sleep(8)
        print("He has come")
        print("Now you are fighting")
        time.sleep(2)
        print("You win")
        print("This is the only way to win")
        print("Congrats! :}")
    else:
        print("Ok telling")
        time.sleep(2)
        print("told")
        print("Now theres an Earthquake and you die in it")
        print("Thanks for playing %s or %s" %(d, j))
        exit("Tata, bye-bye")
print("Now before he dies he kill Kris")
print("human-evil's minion sent a message in his phone to human-evil")
print("It will be sent in 1 month(game's time)")
print("1 = Try to break it")
print("2 = Ignore it")
t = int(input("Choose it  "))
if t == 1:
    print("Ok you chose to break it")
else:
    print("Ok ignored")
    print("When you are going Bablu thinks you are a spy of human-evil")
    print("Then he kills you by stabbing your stomach while going")
    print("Thanks for playing %s or %s" %(d, j))
u ={'*':'a', '&':'b', ')':'c', '(':'d', '^':'e', '@':'f', '%':'g', \
    '#':'h', '!':'i', '$':'j', ',':'k', '/':'l', '|':'m', '}':'n', \
    ']':'o', ':':'p', '[':'q', '`':'r', '~':'s', '-':'t', '_':'u', \
    '+':'v', '=':'w', '<':'x', '?':'y', '>':'z'}
print("The thing is written as -; (] !- @!@-^^} (*?~ *@-^` -]||]`]= for human-evil")
print("Bablu said that the only way to crack it is to get it from human-evil's secret hide out")
print("Then another person asks ,'But where is his hide out'")
print("Then Bablu answers ,'No one knows except human-evil and his minions know it'")
print("Then another person tells,'Ok we'll kidnap one")
print("1=[Agree]")
print("2=[Disagree and kill them all]")
print("3=[Run away]")
v = int(input("Choose one  "))
if v == 1:
    d = d.lowercase()
    x = list(d)
    y = len(d)
    if x[y] == 'a':
        print("Good girl :D")
    elif x[y] == 'e':
        print("Good girl :D")
    elif x[y] == 'i':
        print("Good girl :D")
    elif x[y] == 'o':
        print("Good girl :D")
    elif x[y] == 'u':
        print("Good girl :D")
    else:
        print("Good Boy :>")
        "".join(d)
elif v == 2:
    print("When you disagree they shoot you")
    print("thanks for playing this", d, "or", j)
    exit("Tata, bye-bye")
else:
    print("When you run they shoot you")
    print("thanks for playing this", d, "or", j)
    exit("Tata, bye-bye")
print("Now you and your crew go to search for them")
print("You overcome across a house where there are 3 people training in martial arts")
print("And 1 person reading a book")
print("One can be your patner")
print("1st person # Shield #")
print("2nd person # Sword #")
print("3rd person # ninja blades #")
print("4th person # Super smart #")
z = int(input("Choose your patner  "))
print("Ok")
print("You will continue walking")
time.sleep(2)
print("The you see a couple of guards")
aa = int(input("1-bring 'em down, 2-die, 3-run"))
if aa == 1:
    print("Ok trying")
    time.sleep(2)
    print("You got half down and your patner got the other half")
    print("You go in")
    print("You see a minion of human-evil(h-e)")
    print("What do you do")
    ab = int(input("1-bring him down, 2-die, 3-run"))
    if ab != 1:
        print("Ok")
        if ab ==2:
            print("dead")
        else:
            print("He shoots you while you are running")
        print("Thanks for playing %s or %s" %(d, j))
        exit("Tata, bye-bye")
    else:
        print("You bring him down")
        print("Now only 5 members including you and your patner are left in your crew")
elif aa ==2:
    print("dead")
    print("Thanks for playing %s or %s" %(d, j))
else:
    print("Your patner killed you")
    print("Because he doubted you")
print("You go deeper inside")
print("You see ")
time.sleep(2)
print("...HUMAN-EVIL...")
print("1 = fight him")
print("2 = Die on spot")
print("3 = Run away")
ac = int(input("What is your unanimous decision "))
if ac == 1:
    print("Ok fighting")
    time.sleep(5)
    if z == 1:
        print("You killed him :~}")
        print("You and your patner won")
    else:
        print("You died")
        print("Cause you couldn't co-ordinate well")
        print("If you had chosen shield as your patner you would win")
        print("Thanks for playing this %s or %s" %(d, j))
        exit("Tata, bye-bye")
elif a == 2:
    print("Dead")
    print("Thanks for playing this %s or %s" %(d, j))
    exit("Tata, bye-bye")
else:
    print("Now human-evil shoots you while you are running")
    print("Thanks for playing this %s or %s" %(d, j))
    exit("Tata, bye-bye")
print("Woo-hoo")
print("You and your patner co-ordinated amazingly")
print("Now you find a note in human-evil's pocket")
print("It has the code to the secret code")
print("1 -Crack it-")
print("2 -Ignore it-")
ad = int(input("What to do  "))
if ad == 1:
    ag = time.time()
    print("Ok picked")
    print("It says -;")
    print(u)
    print("The code is -;")
    print("(] !- @!@-^^} (*?~ *@-^` -]||]`]=")
    ae = 0
    while(ae < 1000):
        ae = ae+1
        print(u)
        af = input("What is the code  ")
        af = af.lowercase()
        if af == "do it fifteen days after tommorow":
            print("It is correct!")
            print("Bravo!")
            print("You are super intelligent")
            ah = time.time()
            print("You cracked it in %d guesses" %(ae))
            print("You took", int(ah-ag),"seconds")
            ae = 1000
        else:
            print("It's wrong")
else:
    print("Ok ignored")
    print("Now you got your super powers back")
    print("Thanks for playing this %s or %s" %(d, j))
    exit("Tata, bye-bye")
print("Now you got your super powers back")
u ={'*':'a', '&':'b', ')':'c', '(':'d', '^':'e', '@':'f', ';':'g', \
    '#':'h', '!':'i', '$':'j', ',':'k', '/':'l', '|':'m', '}':'n', \
    ']':'o', ':':'p', '[':'q', '`':'r', '~':'s', '-':'t', '_':'u', \
    '+':'v', '=':'w', '<':'x', '?':'y', '>':'z'}
print(u)
print("-#*},~ @]` :/*?!}; %s ]` %s" %(d, j))
exit("-*-* &?^ &?^")