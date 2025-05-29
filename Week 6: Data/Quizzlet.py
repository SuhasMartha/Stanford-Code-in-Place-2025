def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    score = translation_game(translations)
    print("You got "+str(score)+"/8 words correct, come study again soon!")
    
def translation_game(translation):
    score = 0
    for word in translation:
        user_word = input("What is the Spanish translation for " + word + "? ")
        if(user_word == translation[word]):
            print("That is correct!")
            print("")
            score += 1
        else:
            print("That is incorrect, the Spanish translation for " + word + " is " + translation[word] +".")
            print()
    
    return score

if __name__ == '__main__':
    main()
