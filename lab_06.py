
def decode(s):
    result = ""
    for i in s:
        if int(i) > 3:
            result += str(int(i) - 3)
        else:
            result += str((int(i) + 10) - 3)
    return result



prompt_continue = True
while prompt_continue:
    menu = "Menu\n------------\n1. Encode\n2. Decode\n3. Quit\n"
    print(menu)
    option = int(input("Please enter an option: "))
    if option == 1:
        original = int(input("Please enter your password to encode: "))
        print("Your password has been encoded and stored!")
        encode = original + 33333333
        option_1 = True
        print(menu)
        option = int(input("Please enter an option: "))
        while option_1:
            if option == 2:
                print(f"The encoded password is {encode}, and the original password is {original}.")
                print(menu)
                option = int(input("Please enter an option: "))
    if option == 3:
        prompt_continue = False