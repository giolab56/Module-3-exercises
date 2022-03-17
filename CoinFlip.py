#Coin Flip

import random

heads = 0
tails = 0
flips = 0

while flips < 100:
    coin = random.randint(1,2)

    if coin == 1:
        heads += 1
        flips += 1

    elif coin == 2:
        tails += 1
        flips += 1

print("Coin landed heads", heads, "times")
print("Coin landed tails", tails, "times")