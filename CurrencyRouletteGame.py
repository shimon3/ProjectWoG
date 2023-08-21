from currency_converter import CurrencyConverter
import random

def get_money_interval(difficulty):
    c = CurrencyConverter()
    rate = c.convert(1, 'USD', 'ILS')
    usd = int(random.uniform(1, 100))
    total_value = int(rate) * usd
    low = int(total_value - (5 - difficulty))
    high = int(total_value + (5 - difficulty))
    return total_value ,low ,high

# def get_guess_from_user(usd,low,high):
#          correct_guess = False
#          while not correct_guess:
#              guess = int(input("Guess the value of usd$ in ILS: "))
#              if guess == usd :
#                  print("You guessed the correct number!")
#                  correct_guess = True
#              elif guess>=low:
#                  print("You entered a larger number!")
#              elif guess<=high:
#                  print("You entered a smaller number!")
#              else:
#                  print("Try again!")
#                  return guess,correct_guess
#
# print (get_guess_from_user())
def get_guess_from_user(usd):
    # User needs to guess the Value to a given amount of USD
    while True:
        try:
            guess = int(input(f"Guess the value of {usd}$ in ILS: "))
        except ValueError:
            print("Error: Enter just numbers please, not letters, words ,etc...")
            continue
        return guess