# This is a sample Python script that takes  a users details and automatically generates a password.
# different functions can be created or modified
import random
import string

special_characters = list(string.ascii_letters + string.digits + "!@#$%^&*()/|;'`~-_")


# What if we did this with a customisable length
def password_gen():
    try:
        # length of password entered by user
        length = int(input("Enter password length: "))

        # A normal password should contain at-least 8 characters
        # Let's try to specify it
        if length <= 7:
            return print("Enter a number above 8")

        elif length >= 8:
            print("What where you waiting for goat")

            # shuffling the special_characters
            random.shuffle(special_characters)

            # picking random special_characters from the list
            password = []
            for i in range(length):
                password.append(random.choice(special_characters))

            # shuffling the resultant password
            random.shuffle(password)

            # converting the list to string
            # printing the list
            print("".join(password))
            return password_gen()
        else:
            return print("Oga is everything alright with you?😂")
    except ValueError:
        print('please enter intergers')

password_gen()
# Press the green button in the gutter to run the script.
