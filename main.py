# Michael Huang
import os
import getpass


def image_man(chances=0):
    body_tuple = (" 0 ", "|", "-", "/ ", "\\")
    structure = ["\nPre-Game: ", "------", "|    |", "|   ", "|   ", "|   "]

    # TODO Make it cleaner Aug-14-2021
    if chances == 1:
        structure[3] = structure[3] + body_tuple[0]

    elif chances == 2:
        structure[3] = structure[3] + body_tuple[0]
        structure[4] = structure[4] + " " + body_tuple[1]

    elif chances == 3:
        structure[3] = structure[3] + body_tuple[0]
        structure[4] = structure[4] + body_tuple[2] + body_tuple[1]

    elif chances == 4:
        structure[3] = structure[3] + body_tuple[0]
        structure[4] = structure[4] + body_tuple[2] + body_tuple[1] + body_tuple[2]

    elif chances == 5:
        structure[3] = structure[3] + body_tuple[0]
        structure[4] = structure[4] + body_tuple[2] + body_tuple[1] + body_tuple[2]
        structure[5] = structure[5] + body_tuple[3]

    elif chances == 6:
        structure[3] = structure[3] + body_tuple[0]
        structure[4] = structure[4] + body_tuple[2] + body_tuple[1] + body_tuple[2]
        structure[5] = structure[5] + body_tuple[3] + body_tuple[4]

    for i in structure:
        print(i)


def clear():
    os.system("clear")


def input_validation():
    image_man()

    print("\nPlease enter the word for the game to start.")
    user_input = getpass.getpass("Word(s): ", stream=None).upper()

    stuff = True

    while stuff:
        try:
            if ord(user_input[0]) == 32:
                clear()
                image_man()

                print("\nPlease try again.  you only enter a space")
                user_input = getpass.getpass("Word(s): ", stream=None).upper()

        except IndexError:
            clear()
            image_man()

            print("\nPlease input something.")
            user_input = getpass.getpass("Word(s): ", stream=None).upper()

        else:
            return user_input


def count_words(word):
    amount = []

    str_vis = []

    for iteration in range(len(word)):

        upper_word = word[iteration].upper()

        amount.append(upper_word)

        if ord(upper_word) == 32:
            str_vis.append(" ")

        elif ord(upper_word) < 65 or ord(upper_word) > 90:
            str_vis.append(upper_word)

        else:
            str_vis.append("_")

    return amount, str_vis


def the_imagineers(bucket_strings, view):
    player_input = str(input()).upper()

    game_on = True

    while game_on:
        try:
            clear()
            image_man(view)

            print(' '.join(bucket_strings))

            # White-Space
            if ord(player_input[0]) == 32:

                print("Please enter a Character.  Not White Space.")
                player_input = str(input()).upper()

            # Repeating Words
            while player_input in bucket_strings:
                clear()
                image_man(view)

                print("Please try a different character.")
                print("Words already used: ", " ".join(bucket_strings))
                player_input = str(input()).upper()
            else:
                bucket_strings.append(player_input)

        # Entering without inputting something.
        except IndexError:

            print(' '.join(bucket_strings))

            print("Please enter something.")
            player_input = str(input()).upper()

        else:
            return player_input, bucket_strings


def checking(attempt, trys, answer, hidden_answer):

    if len(trys) > 1:
        try:
            for items in range(len(answer)):
                if trys[items] != answer[items]:
                    print(trys[items], " ", answer[items])
                    attempt += 6

                for i in range(len(answer)):
                    if trys[i] in answer[i]:
                        hidden_answer[i] = trys[i]
        except IndexError:
            attempt += 6

    if len(trys) == 1:
        for i in range(len(answer)):
            if trys in answer[i]:
                hidden_answer[i] = trys

        if trys not in answer:
            attempt += 1

    return attempt, hidden_answer


def keep_playing():
    print("Do you want to play again?  Yes or No.")

    game_input = str(input()).upper()

    while game_input[0] != 'Y' and game_input[0] != 'N':
        print("Please enter yes or no.")
        game_input = str(input()).upper()

    return game_input[0] == 'Y'


# def cleaner(strings):
#     shine = []
#
#     for i in range(len(strings)):
#         for items in range(len(strings)):
#             if strings[i] == strings[items] and i != items:
#                 pass
#             else:
#                 shine.append(strings[i])
#
#     return shine


def main():

    game = True
    while game:
        clear()

        # Input
        word_of_day = input_validation()

        amount_str, visible_str = count_words(word_of_day)

        # Processing
        live = 0
        used_words = []
        alive = True
        while alive:

            print(''.join(visible_str), "\n")

            print("Please guess a letter or the entire word.  If entire words include spaces.")

            imagineering, used_words = the_imagineers(used_words, live)

            live, visible_str = checking(live, imagineering, amount_str, visible_str)

            clear()
            image_man(live)

            # clean = cleaner(used_words)

            print("Words already used: ", " ".join(used_words))  # TODO fix clean

            print("Current input: ", imagineering)

            # Output
            if "_" not in visible_str:
                print("\n*You won*")
                print("Word: ", ''.join(amount_str), "\n")
                alive = False

            elif live >= 6:
                print("\n*You lose*")
                print("Word: ", ''.join(amount_str), "\n")
                alive = False
            else:
                continue

        game = keep_playing()


main()
