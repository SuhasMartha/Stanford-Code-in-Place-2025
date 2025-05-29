#Write a console program which asks the user for their height in meters and prints whether or not they are the correct height to be a NASA astronaut.

def main():
    height = float(input("Enter your height in meters: "))
    
    if height > 1.6 and height < 1.9:
        print("Correct height to be an astronaut")
    elif height <= 1.6:
        print("Below minimum astronaut height")
    else:  # height >= 1.9
        print("Above maximum astronaut height")

if __name__ == "__main__":
    main()
