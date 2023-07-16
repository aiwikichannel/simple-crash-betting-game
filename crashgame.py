import random
import time

print("Welcome to Crash!")

cash = 100 # starting cash amount
print(f"You have ${cash} remaining")

bet = int(input("How much would you like to bet? "))

cash -= bet
print(f"You have ${cash} remaining")

payout = 1.5 # starting payout multiplier 

while True:

  # increase payout multiplier
  payout += round(random.uniform(0.05, 0.15), 2) 

  print(f"Current payout: {payout}x")

  # check for crash
  if random.random() <= 1/payout:
    print("Game crashed!")  
    break

  # give user option to cash out
  print("Press enter to cash out, or type 'roll' to keep going...")
  choice = input()
  if choice == '':
    cash += bet * payout
    print(f"You cashed out at {payout}x and won {bet * payout}")
    break

  time.sleep(0.5)

print(f"You have ${cash} remaining")