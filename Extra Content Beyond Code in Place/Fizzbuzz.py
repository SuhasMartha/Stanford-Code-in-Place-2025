def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Fizzbuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

def main():
    for i in range(1, 18):  # 1 to 17 inclusive
        print(fizzbuzz(i))

if __name__ == '__main__':
    main()
