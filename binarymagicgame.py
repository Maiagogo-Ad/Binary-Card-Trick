cards = {
    1 : """
| 01 17 05 07 47 45 |
| 27 57 61 39 03 13 |
| 53 21 19 31 29 49 |
| 63 55 33 43 41 11 |
| 35 59 37 23 25 09 |
        15 51
    """,

2 : """
| 02 58 55 10 11 27 |
| 22 30 18 14 46 26 |
| 35 51 34 59 07 42 |
| 54 39 31 50 47 62 |
| 19 38 15 03 43 23 |
        63 06
    """,

4 : """
| 04 55 07 47 36 63 |
| 53 39 13 21 37 23 |
| 15 12 52 31 06 20 |
| 45 05 22 28 29 30 |
| 60 14 61 44 62 38 |
        54 46
    """,

8 : """
| 08 56 42 44 24 28 |
| 15 13 45 43 46 09 |
| 14 61 31 63 41 47 |
| 11 60 59 40 27 26 |
| 30 10 29 25 62 57 |
        12 58
    """,

16 : """
| 16 30 31 26 62 21 |
| 22 48 58 56 27 19 |
| 54 28 59 18 20 52 |
| 53 25 60 51 49 57 |
| 50 55 61 17 29 63 |
        23 24
    """,
32 : 
"""
| 32 58 56 51 57 59 |
| 54 52 36 61 45 42 |
| 63 60 34 35 53 33 |
| 37 38 44 48 50 49 |
| 41 40 43 39 55 47 |
        62 46
    """
}

def get_valid_choice(choice):
    while True:
        valid_choices = ("y", "n")
        if choice not in valid_choices:
            print("Invalid choice")
            choice = input("is the number appear? Yes or No (y/n): ").lower().strip()
            continue    

        return choice
    
def display_rules():
    print("="*73)
    print("Chose a number between 1 to 63 in your mind")
    print("Check the card if the number appear on the card press y otherwise press n")
    print("="*73)

def play_game(cards):
    counter = 1
    is_appeared = []
    for number, card in cards.items():
        print("="*21)
        print(f"     Card {counter}    ")
        print("="*21)
        print(card)
        user_choice = get_valid_choice(input("is the number appear? Yes or No (y/n): ").strip().lower())
        
        if user_choice == "y":
            is_appeared.append(number)

        counter += 1
    
    return is_appeared
    
def calculate_result(appeared_numbers):

    total = sum(appeared_numbers)

    return total

def save_result(number):
    with open("result.txt", "w") as file:
        file.write("\n==================")
        file.write(f"\nYour Number is {number}")
        file.write("\n==================")
    print("Your file save successfully")
        


def main():
    while True:
        print("="*34)
        print("WELCOME TO BINARY CARD MAGIC TRICK")
        print("="*34)

        game = {
            "1" : "Rules of the Game",
            "2" : "Play Game",
            "3" : "Exit"
        }

        for num, value in game.items():
            print(num, value)
        
        choice = input("Enter choice: ")

        if choice == "1":
            display_rules()

        elif choice == "2":
           list_of_numbers = play_game(cards)
           mind = calculate_result(list_of_numbers)
           save_result(mind)
           
        elif choice == "3":
            print("Goodbye")
            break

        else:
            print("Invalid choice")

    
if __name__ == "__main__":
    main()