print(" Welcome to the quiz Show ")
cash = 0
for i in range(5):
  if i == 0:
    z=input("'What is the name of the oldest lake in the world?'\n")
    if z == "Lake Baikal":
      print("Correct Answer")
      print("YOU WoN 1,000 Rupees")
      cash = 1000
    else:
      print("Wrong Answer")
  if i == 1:  
    z=input("'Where on the body would one find the orbit?'\n")
    if z== "Eye (the socket)":
      print("Correct Answer") 
      print("YOU WoN 1,000 Rupees")
      cash = 1000 + cash
    else:
      print("Wrong Answer")
  if i == 2:  
    z = input("How many rings does the planet Saturn have?'\n")
    if z == "Seven":
      print("Correct Answer")
      print("YOU WoN 1,000 Rupees")
      cash = 1000 + cash
    else:
      print("Wrong Answer")
  if i == 3:  
    z = input("'What type of tree is pictured on the Lebanese flag?'\n")
    if z == "Cedar tree":
      print("Correct Answer")
      print("YOU WoN 1,000 Rupees")
      cash = 1000 + cash
    else:
      print("Wrong Answer")
  if i == 4:  
    z = input("'How old was Queen Victoria when she died?'\n")
    if z == "81":
      print("Correct Answer")
      print("YOU WoN 1,000 Rupees")
      cash = 1000 + cash
    else:
      print("Wrong Answer")
print("You Won",cash,"Rupees")
    
   
  