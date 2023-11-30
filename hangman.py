import random
print("Guess the name of the animal:")
lir= ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
li=list(lir[random.randint(0,len(lir))])
s="_"*len(li)
li1=list(s)
listhangman=["  +---+ \n  |   |\n      |\n      |\n      |\n      |\n=========","  +---+ \n  |   |\n  o   |\n      |\n      |\n      |\n=========","  +---+ \n  |   |\n  o   |\n  |   |\n      |\n      |\n=========","  +---+ \n  |   |\n  o   |\n /|   |\n      |\n      |\n=========","  +---+ \n  |   |\n  o   |\n /|\  |\n      |\n      |\n=========","  +---+ \n  |   |\n  o   |\n /|\  |\n /    |\n      |\n=========","  +---+ \n  |   |\n  o   |\n /|\  |\n / \  |\n      |\n========="]
j=0
while True:
    letter=input("Enter letter:")
    if letter in li:
        i=li.index(letter)
        li1[i]=letter
        ss="".join(li1)
        print(ss)
        ss=" "
        li[i]="_"
        if "_" not in li1:
            print("congrats")
            break
    elif j==7:
        print("game over!")
        break
    else:
        print(listhangman[j])
        print("Wrong!!Try again")
        j+=1
    