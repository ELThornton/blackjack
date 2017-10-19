# Elena Thornton
# 10/19/27
# This program plays a simplified version of Black Jack or 21 with the user.
# Black Jack.py

import random
# This generates random numbers.


def get_a_card():
    """
    This function set up getting numbers in the future
    :return: number_1
    """
    number_1 = random.randint(1, 11)
    return number_1


def show_total(number_1, number_2):
    """
    This function totals the values of number_1 and number_2
    :param number_1: this is a get card
    :param number_2: this is a get card
    :return: total
    """
    total = number_1 + number_2
    print("the sum for your first two cards is", total)
    return total


def ask_user_if_they_want_another_card(player_total):
    """
    This function ask the play if they want another card or not.
    Then it adds the new card to the old total and give them their new total.
    :param player_total: this is the total of number_1 and number_2
    :return: new_total
    """
    users_answer = input("do you want another card?:",)
    if users_answer == "yes":
        new_total = player_total + get_a_card()
        print(new_total, "is your new total")
    else:
        new_total = player_total
        print("okay moving on")
    return new_total


def get_computer_total():
    """
    This get the computers total.
    :return: computer_total
    """
    number_3 = get_a_card()
    number_4 = get_a_card()
    computer_total = number_3 + number_4
    print("my card total is", computer_total)
    return computer_total


def compare_totals(player_new_total, comp_total):
    """
    This compares the card totals. It also tell the player if they win.
    :param player_new_total: this is the players card total.
    :param comp_total: this is the computers card total.
    :return: none
    """
    if player_new_total > comp_total and player_new_total <= 21:
        print("congratulation you win!")
    else:
        print("sorry you lose.")


def main():
    number_1 = get_a_card()
    number_2 = get_a_card()
    player_total = show_total(number_1, number_2)
    player_new_total = ask_user_if_they_want_another_card(player_total)
    comp_total = get_computer_total()
    compare_totals(player_new_total, comp_total)

main()
