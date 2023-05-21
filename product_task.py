# Arundhathi-B

from math import ceil

def getInput():
  items, wraps = [], []
  
  for i in range(3):
    items.append(int(input(f"No of units required for product {chr(65 + i)}: ")))
    wraps.append(input("Should be gift wrapped (yes/no): "))
   
  return items, wraps
  
def calculateCost(prices, items):
    costs, subtotal = [], 0
    
    for i in range(3):
        cost_per_product = items[i]*prices[i]
        costs.append(cost_per_product)
        subtotal += cost_per_product
        
    return costs, subtotal
  
def applyDiscount(items, prices, subtotal):
      discounts = []
      total_quantity = sum(items)
      
      if subtotal > 200:
          discounts.append((subtotal - 10, "flat_10_discount"))
          
      if total_quantity > 20:
          discounts.append((subtotal - 0.1*subtotal, "bulk_10_discount"))
          
      new_price = 0
      for i in range(3):
          cost_per_product = items[i]*prices[i]
          
          if items[i] > 10:
              reduced_price = 0.5*cost_per_product
              new_price += reduced_price
              
          else:
              new_price += cost_per_product
              
      if not int(new_price) is subtotal:
          discounts.append((new_price, "bulk_5_discount"))
          
      if total_quantity > 30:
          new_price = 0
          for i in range(3):
              if items[i] > 15:
                  extra_items = items[i] - 15
                  new_price += (15*prices[i]) + 0.5*extra_items*prices[i]
                  
              else:
                  new_price += items[i]*prices[i]
                  
          if not int(new_price) is subtotal:
              discounts.append((new_price, "tiered_50_discount"))
              
      best_offer = min(discounts)
      
      print(f"Discount applied: {best_offer[1]}")
      print(f"Discount price: {best_offer[0]}")
      
      return best_offer[0]
    
    
def finalPrice(items, wraps, offer_price):
    total_units = sum(items)
    gift_wraps = 0
    
    for i in range(3):
        if wraps[i] =="yes":
            gift_wraps += items[i]
            
    shipping_fee = ceil(total_units/10)
    final_price = offer_price + gift_wraps + shipping_fee
    print(f"gift wrap fee: {gift_wraps}")
    print(f"shipping fee: {shipping_fee}")
    print(f"final price: {final_price}")
    
    
def showOutput(items, costs, subtotal):
    for i in range(3):
        print(f"product {chr(65 + i)}")
        print("======================")
        print(f"quantity: {items[i]}")
        print(f"total amount: {costs[i]}")
        print("======================")
        
    print(f"subtotal: {subtotal}")
    
def main():
    prices = [20, 40, 50]
    items, wraps = getInput()
    costs, subtotal = calculateCost(prices, items)
    showOutput(items, cost, subtotal)
    offer_price = applyDiscount(items, prices, subtotal)
    finalPrice(items, wraps, offer_price)
    
    
    
main()
