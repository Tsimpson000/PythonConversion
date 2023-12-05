class Player:
    def __init__(player, name, number):
        player.name = name
        player.number = number
    def displayPlayer(player):
        print("Name - " + player.name + " Number - " + str(player.number))
p1 = Player("Shiva", 45)

p2 = Player("Tyler", 30)

p3 = Player("Fluffy", 36)

p4 = Player("Odin", 100)

p5 = Player("Tinsil", 85)

pList = [p1, p2, p3, p4, p5]

print("Players")
print("1 - Display Players")
print("2 - Display Players with an Odd letter")
print("3 - Display Players starting with a letter")
print("4 - Add Player")
print("Enter your choice")

userNum = int(input())

print(userNum)


if userNum == 1:
    for player in pList:
        print(player.displayPlayer())
elif userNum == 2:
    for player in pList:
        if player.number % 2 != 0:
            print(player.displayPlayer())
#  elif userNum == 3:
#  elif userNum == 4:
else:
    print("Invalid input")
