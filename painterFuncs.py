def intro():
    """
    Provides an introduction to the ASCII Art Painter program and prompts the user for their choice of art and border character.
    
    Returns:
        int: The user's choice of art (1-4).
        str: The user's choice of border character.
    """
    print("Welcome to the ASCII Art Painter!")
    print("Choose an art:")
    print("1. Sleeping Cat")
    print("2. Sailing Ship")
    print("3. Custom Art 1")
    print("4. Custom Art 2")
    while True:
        choice = int(input("Enter your choice (1-4): "))
        if choice in [1, 2, 3, 4]:
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")
    while True:
        border = input("Enter the border character (special character only): ")
        if len(border) == 1 and not border.isalnum():  # Check if it's a single special character
            break
        else:
            print("Please enter only one special character.")
    return choice, border

def printHeaderFooter(border, size):
    """
    Prints the header and footer lines using the specified border character and size.

    Parameters:
        border (str): The border character.
        size (int): The size of the line.
    """
    print(border * size)

def sleepingCat(border):
    """
    Prints an ASCII art of a sleeping cat.

    Parameters:
        border (str): The border character.
    """
    cat = [
        "   |\\      _,,,---,,_",
        "ZZZzz /,`.-'`'    -.  ;-;;,_",
        "     |,4-  ) )-,_. ,\\ (  `'-",
        "    '---''(_/--'  `-'\\_)"
    ]
    size = len(cat[0]) + 2  # considering border
    printHeaderFooter(border, size)
    for line in cat:
        print(border + line + border)
    printHeaderFooter(border, size)

# Define other functions for sailingShip, customArt1, customArt2, and blank...
def sailingShip(border):
    ship = [
        "               /\\     ",
        "      ________/  \\_   ",
        " ____/               \\ ",
        "|    \\_______________/",
        "|                      ",
        "|  |\\ \\ \\ \\ \\ \\ \\ \\  | ",
        "|  | \\ \\ \\ \\ \\ \\ \\ \\ | ",
        "|  | |\\ \\ \\ \\ \\ \\ \\ \\| ",
        "|  | | \\ \\ \\ \\ \\ \\ \\ \\| ",
        "|  | |  |\\ \\ \\ \\ \\ \\ \\ ",
        "|  | |  | \\ \\ \\ \\ \\ \\ \\",
        "|  | |  | | | | | | | |",
        "|__|_|__|_|_|_|_|_|_|_|"
    ]
    size = len(ship[0]) + 2  # considering border
    printHeaderFooter(border, size)
    for line in ship:
        print(border + line + border)
    printHeaderFooter(border, size)

def customArt1(border):
    art = [
                  ";,",
     "_o_    ;:;",
 ",-. ---`.__ ;",
"((j`=====,-",
 "`-\     /",
    "`-=-"   
    ]    
    size = len(art[0]) + 2  # considering border
    printHeaderFooter(border, size)
    for line in art:
        print(border + line + border)
    printHeaderFooter(border, size)

def customArt2(border):
    art = [
        "  /\\_/\\",
        " ( o.o )",
        "  > ^ < ",
        " /  ~  \\",
        "/_/ \\_\\"
    ]
    size = len(art[0]) + 2  # considering border
    printHeaderFooter(border, size)
    for line in art:
        print(border + line + border)
    printHeaderFooter(border, size)


def blank(border):
    size = 7  # considering border
    printHeaderFooter(border, size)
    for _ in range(5):
        print(border + "     " + border)
    printHeaderFooter(border, size)