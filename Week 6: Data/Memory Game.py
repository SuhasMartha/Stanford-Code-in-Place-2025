import random
NUM_PAIRS = 3

def main():
    truths = []
    index = 0
    value = 0
    for i in range(NUM_PAIRS): 
        truths.insert(index, value)
        index += 1
        truths.insert(index, value)
        index += 1
        value += 1
    
    random.shuffle(truths)
    
    display = []
    for i in range(NUM_PAIRS *2):
        display.append('*')

    while "*" in display:
        print(display)

        user_index1 = get_valid_index(display)
        user_index2 = get_valid_index(display)
        while user_index1 == user_index2:
            print("You entered the same index twice. Try again.")
            user_index2 = get_valid_index(display)

        value1 = truths[user_index1]
        value2 = truths[user_index2]
        if value1 == value2:
            display[user_index1] = value1
            display[user_index2] = value2
            print("Match!")
            clear_terminal()
        else: 
            print(f"Value at index {user_index1} is {value1}")
            print(f"Value at index {user_index2} is {value2}")
            print("No match. Try again.")
            input("Press Enter to continue...")
            clear_terminal()
    
    print(display)
    print("Congratulations! You won!")

def get_valid_index(display):
    while True:
        user_index = input("Enter an index: ")

        if not user_index.isdigit():
            user_index =  input("Not a number. Try again.")
            continue

        user_index = int(user_index)

        if user_index > (NUM_PAIRS * 2 - 1):
            user_index =  input("Invalid index. Try again.")
            continue

        if display[user_index] != "*":
            user_index = input("This number has already been matched. Try again.")
            continue

        return user_index

def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()
