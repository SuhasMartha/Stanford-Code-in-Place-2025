#Print out each of the numbers 1 through 100 and whether that number is even or odd.


MAX_NUMBER = 100

def main():
    for number in range(1, MAX_NUMBER + 1):
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")

if __name__ == "__main__":
    main()
