# Arundhathi-B

from math import ceil

def getInput():
  items, wraps = [], []
  
  for i in range(3):
    items.append(int(input(f"No of units required for product {chr(65 + i)}: ")))
    wraps.append(input("Should be gift wrapped (yes/no): "))
