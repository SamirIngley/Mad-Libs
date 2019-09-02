
import random

print("~ ~ MaDliBs ~ ~")
print ("Give me five single nouns: ")
nouns = [input(), input(), input(), input(), input()]


def randomize(aray):
    random.shuffle(aray)

def kill():
    print("Follow the instructions.")
    exit()


def show():
    print("______________________________________________________")
    print(pronouns[0] + " went to the store today to buy themself a " + nouns[0] + ".")
    print(pronouns[1] + " wore it to my neice's party where the " + adjectives[2] + " balloons ")
    print("and " + adjectives[0] + " house were calling his name. After, the ")
    print("magic " + nouns[2] + " was spectacular and full of surprises. ")
    print("We spent the day eating " + adjectives[1] + " " + nouns[3] + " and " + nouns[4])
    print("from the pinata. We fell asleep watching " + plural_nouns[0] + ".")


if (nouns[0].isdigit() or nouns[1].isdigit() or nouns[2].isdigit() or nouns[3].isdigit() or nouns[4].isdigit()):
    kill()
else:
    randomize(nouns)
    print("Gimme a plural noun.. ")
    plural_nouns = [input()]
    if (plural_nouns[0].isdigit()):
        kill()
    else:
        randomize(plural_nouns)
        print("Gimme three adjectives.. ")
        adjectives = [input(), input(), input()]
        if (adjectives[0].isdigit() or adjectives[1].isdigit() or adjectives[2].isdigit()):
            kill()
        else:
            randomize(adjectives)
            print("Gimme two pronouns..")
            pronouns = [input(), input()]
            if (pronouns[0].isdigit() or pronouns[1].isdigit()):
                kill()
            else:
                randomize(pronouns)


show()
