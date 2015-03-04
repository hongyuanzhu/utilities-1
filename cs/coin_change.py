import pandas as pd
import numpy as np


def round_up(amt, min_denomination):
    if amt <= min_denomination:
        return min_denomination
    
    mod = amt % min_denomination
    if mod == 0:
        return amt
    else:
        return min_denomination * (int(amt / min_denomination)+1)
        
def change_maker(





# create a map: key - drug name, value - denominations of mg amounts

# change maker that stores which coins are needed to make change

# round up drug amount

# run change_maker function on rounded up drug amount







