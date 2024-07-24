def encode(num):
    encoded_num = ''
    for char in num:
        encoded_num += str((int(char) + 3) % 10)
    return encoded_num
def decode(number):
    result = ''
    for char in number:
        result += str((int(char) - 3) % 10)
    return result


def main():
    StoredNum = ''
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == "1":
            userinput = input("Please enter the password to encode: ")
            StoredNum = encode(userinput)
            print("Your password has been encoded and stored!")
        elif choice == "2":
            if StoredNum:
                original = decode(StoredNum)
                print(f"The encoded password is {StoredNum}, and the original password is {original}.")
            else:
                print("No encoded password stored yet. Please encode a password first.")
        elif choice == "3":
            break

        else:
            print("Please enter a valid option")

if __name__ == "__main__":
    main()