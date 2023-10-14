"""
This program generates a dungeon using Bowyer-Watson's and Prim's algorithms.
By default the program uses a 900px/500px display where it generates 12 rooms
connected by hallways. Rooms can't be generated within 80 pixels of each other and
therefore a limit for the number of rooms is given for every input.
 
"""

from dungeon_generator import dungeon_generator

def main():
    print(
        "Welcome to the dungeon generator!\n"
        "\n"
        "Press 1 to read the manual\n"
        "Press 2 to start\n"
        "Press any other key to quit"
    )
    while True:
        
        user_input = input("Input: ")

        if user_input == "1":
            guide()
        elif user_input == "2":
            get_input()
        else:
            break
            

def get_input():
    while True:
        width = int(input("Choose a width: "))

        if width < 400:
            print(f"{width} is too narrow")
            continue

        height = int(input("Choose a height: "))

        if height < 300:
            print(f"{height} is too low")
            continue

        nodes = int(input("How many rooms: "))

        if nodes < 3:
            print(f"{nodes} is not enough")
            continue

        print("")
        print("Press 1 to generate a new dungeon")
        print("Press 2 to give a new input")
        print("Press 3 to quit")

        program = dungeon_generator(nodes, width, height)
        if program == 1:
            continue

def guide():
    print(
        "\n"
        "This program generates a dungeon with rooms connected by hallways.\n"
        "Give the program values for height and width and then choose how\n"
        "many rooms will be generated. The dungeon must be at least 400 pixels\n"
        "wide and 300 pixels tall. If you give an invalid input, the program\n"
        "will let you know. Have fun!"
        "\n"
    )

if __name__ == '__main__':
    main()
