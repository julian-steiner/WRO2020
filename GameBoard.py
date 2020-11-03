from DriveTrain import DriveTrain
import RobotContainer as rc
class Gameboard:
    house_c = ""
    bricks_c = ""
    humans_c = ""
    sand_c = ""
    houses = [0, 0, 0, 0]
    sand = [0, 0, 0, 0]
    bricks = [0, 0, 0, 0]
    humans = [0, 0, 0, 0]
    deliveredBlocks = []
    deliveredBags = []
    stage = 0
    rc = rc.RobotContainer()
    
    @staticmethod
    def update():
        #Autofill nones
        if(Gameboard.houses.count("Green") + Gameboard.houses.count("Blue") == 2 and Gameboard.houses.count(0) != 0):
            for i in range(Gameboard.houses.count(0)):
                Gameboard.houses[Gameboard.houses.index(0)] = "None"

        if(Gameboard.bricks.count("Yellow") + Gameboard.bricks.count("Red") == 2 and Gameboard.bricks.count(0) != 0):
            for i in range(Gameboard.bricks.count(0)):
                Gameboard.bricks[Gameboard.bricks.index(0)] = "None"
        
        if(Gameboard.humans.count("Yellow") + Gameboard.humans.count("Red") == 2 and Gameboard.houses.count(0) != 0):
            for i in range(Gameboard.bricks.count(0)):
                Gameboard.bricks[Gameboard.bricks.index(0)] = "None"

        if(Gameboard.sand.count("Green") + Gameboard.sand.count("Blue") == 2 and Gameboard.sand.count(0) != 0):
            for i in range(Gameboard.sand.count(0)):
                Gameboard.sand[Gameboard.sand.index(0)] = "None"

        #Autofill Nones in Bricks and Houses
        if(Gameboard.bricks.count("Yellow") + Gameboard.bricks.count("Red") != 2 and Gameboard.bricks.count("None") < 2):
            for i in range(4):
                if(Gameboard.houses[i] in ["Green", "Blue"]):
                    Gameboard.bricks[i] = "None"
                    Gameboard.sand[i] = "None"
        
        #Autofill Nones in Humans
        if(Gameboard.humans.count("Yellow") + Gameboard.humans.count("Red") != 2 and Gameboard.humans.count("None") < 2):
            for i in range(4):
                if(Gameboard.houses[i] in ["None"] or Gameboard.bricks[i] in ["Yellow", "Red"]):
                    Gameboard.humans[i] = "None"

        #Autofill colors

        #Autofill houses
        if(Gameboard.houses.count(0) == 1):
            c = "None"
            if(Gameboard.house_c == "Blue"):
                c = "Green"
            else:
                c = "Blue"
            Gameboard.houses[Gameboard.houses.index(0)] = c
        
        #Autofill  bricks
        if(Gameboard.bricks.count(0) == 1):
            c = "None"
            if(Gameboard.bricks_c == "Yellow"):
                c = "Red"
            else:
                c = "Yellow"
            Gameboard.bricks[Gameboard.bricks.index(0)] = c
        
        #Autofill humans
        if(Gameboard.humans.count(0) == 1):
            c = "None"
            if(Gameboard.humans_c == "Yellow"):
                c = "Red"
            else:
                c = "Yellow"
            Gameboard.humans[Gameboard.humans.index(0)] = c
        
        #Autofill sandbags
        if(Gameboard.sand.count(0) == 1):
            c = "None"
            if(Gameboard.sand_c == "Blue"):
                c = "Green"
            else:
                c = "Blue"
            Gameboard.sand[Gameboard.sand.index(0)] = c
    
    @staticmethod
    def setBrick(position, color):
        Gameboard.bricks[position] = color
        if color != "None":
            Gameboard.bricks_c = color
        Gameboard.update()

    @staticmethod
    def setHouse(position, color):
        Gameboard.houses[position] = color
        if color != "None":
            Gameboard.house_c = color
        Gameboard.update()

    @staticmethod
    def setHuman(position, color):
        Gameboard.humans[position] = color
        if color != "None":
            Gameboard.humans_c = color
        Gameboard.update()

    @staticmethod
    def setSand(position, color):
        Gameboard.sand[position] = color
        if color != "None":
            Gameboard.sand_c = color
        Gameboard.update()

    @staticmethod
    def setBagDelivered(color):
        Gameboard.deliveredBags.append(color)
    
    @staticmethod
    def setBlockDelivered(color):
        Gameboard.deliveredBlocks.append(color)

