def menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')

def encode(password):
    string = ''
    for i in password:
        new = (int(i) + 3) % 10
        string = string + str(new)
    return string

def main():
    choice = 0
    while choice != 3:
        menu()
        choice = int(input('Please enter an option: '))
        if choice == 1:
            password = input('Please enter your password to encode: ')
            encoded_pass = encode(password)
            print('Your password has been encoded and stored!\n')
            continue
        elif choice == 2:
            print(f'The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}.\n')
            continue

if __name__ == '__main__':
    main()