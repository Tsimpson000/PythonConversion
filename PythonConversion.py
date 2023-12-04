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

p1.displayPlayer()
