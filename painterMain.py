import painterFuncs

def main():
    choice, border = painterFuncs.intro()

    if choice == 1:
        painterFuncs.sleepingCat(border)
    elif choice == 2:
        painterFuncs.sailingShip(border)
    elif choice == 3:
        painterFuncs.customArt1(border)
    elif choice == 4:
        painterFuncs.customArt2(border)
    else:
        print("Sorry, we don't seem to have that painting.")
        exit(-1)

    print("Hope you enjoyed your art!")

if __name__ == "__main__":
    main()
