#This creates a list of 1000 strings that are all "H"
#Each string in the list will represent a coin
coins = ["H"] * 1000


#This function will flip a coin by changing a specific string in the coins list
def flip_coin(index):
    if coins[index] == "H":
        coins[index] = "T"
    else :
        coins[index] = "H"
        
        
#This interger is used to find out if the coin is a 2nd, 3rd, 4th etc coin
divisor = 2
 
#This nested for loop is where the simulation happens
#The first loop controls which group of coins is being incremented through by adding 1 to the divisor at the end of each pass
#The second for loop will find out if a coin belongs to that group and then flip it
for _ in range(1000):    
  for i in range(1, 1000):
      if (i + 1) % divisor == 0:
          flip_coin(i)
  divisor = divisor + 1
    
#The enumerate function is used to get the index and the value for the coins list
#If the coin is heads up (value is "H") then its position will be shown
#The coin's position is the index + 1 as the list index starts at 0 
for index, value in enumerate(coins):
  if value == "H":
      print(index + 1)
