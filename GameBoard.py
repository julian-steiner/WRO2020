from DriveTrain import DriveTrain
import RobotContainer as rc
class Gameboard:
    house_c = ""
    bricks_c = ""
    humans_c = ""
    sand_c = ""
    houses = [0, 0, 0, 0]
    house_positions = []
    sand = [0, 0, 0, 0]
    bricks = [0, 0, 0, 0]
    humans = [0, 0, 0, 0]
    house_p = 5
    deliveredBlocks = []
    deliveredBags = []
    deliveredOrders = []
    bricksArranged = []
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
                if(Gameboard.humans[i] == "None"):
                    Gameboard.bricks[Gameboard.bricks.index(0)] = "None"

        if(Gameboard.sand.count("Green") + Gameboard.sand.count("Blue") == 2 and Gameboard.sand.count(0) != 0):
            for i in range(Gameboard.sand.count(0)):
                Gameboard.sand[Gameboard.sand.index(0)] = "None"

        #Autofill Nones in Houses:
        if(Gameboard.houses.count("Blue") + Gameboard.houses.count("Green") != 2 and Gameboard.houses.count("None") < 2):
            for i in range(4):
                if Gameboard.bricks[i] in ["Red", "Yellow"] or Gameboard.sand[i] in ["Green", "Blue"]:
                    Gameboard.houses[i] = "None"

        #Autofill Nones in Bricks and Sand
        if((Gameboard.bricks.count("Yellow") + Gameboard.bricks.count("Red") != 2 and Gameboard.bricks.count("None") < 2) or (Gameboard.sand.count("Green") + Gameboard.sand.count("Blue") != 2 and Gameboard.sand.count("None") < 2)):
            for i in range(4):
                if(Gameboard.houses[i] in ["Green", "Blue"]):
                    Gameboard.bricks[i] = "None"
                    Gameboard.sand[i] = "None"
        
        #Autofill Nones in Humans
        if(Gameboard.humans.count("Yellow") + Gameboard.humans.count("Red") != 2 and Gameboard.humans.count("None") < 2):
            for i in range(4):
                if(Gameboard.houses[i] in ["None"] or Gameboard.bricks[i] in ["Yellow", "Red"]):
                    Gameboard.humans[i] = "None"

        #Autofill HousePositions
        for i in range(4):
            if(Gameboard.houses[i]in ["Blue", "Green"]):
                Gameboard.house_positions.append(i)

        #Predict House
        for i in range(4):
            if(Gameboard.humans[i] not in ["None", 0] and Gameboard.houses[i] == 0):
                Gameboard.house_p = i

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
            Gameboard.bricksArranged = color
        Gameboard.update()

    @staticmethod
    def setHouse(position, color):
        if(color != "None" and Gameboard.house_c != ""):
            if Gameboard.house_c == "Blue":
                color = "Green"
            else:
                color = "Blue"
            
        Gameboard.houses[position] = color
        if color != "None":
            Gameboard.house_c = color
            Gameboard.house_positions.append(position)
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

    @staticmethod
    def setOrderDelivered(checkpoint):
        Gameboard.deliveredOrders.append(checkpoint)

    @staticmethod 
    def getDistance(p1, p2):
        if p1 == p2:
            return 0
        elif p1 in [0, 1] and p2 in [0, 1]:
            return 1
        elif p1 in [2, 3] and p2 in [2, 3]:
            return 1
        else:
            return 2
    
    @staticmethod
    def calculateMove(checkpoint):
        Gameboard.update()
        loaded_bag = rc.RobotContainer.getLoaded()[1]
        loaded_brick = rc.RobotContainer.getLoaded()[2]
        bags = Gameboard.sand
        houses = Gameboard.houses
        house_positions = Gameboard.house_positions
        bricks = Gameboard.bricks
        humans = Gameboard.humans
        deliveredBags = Gameboard.deliveredBags
        deliveredBlocks = Gameboard.deliveredBlocks
        bagDistance = 3
        brickDistance = 3
        print(bags)
        print(bricks)
        print(houses)
        print(humans)

        # #check if robot has to scan the house
        # if houses[checkpoint] == 0:
        #     return [3, checkpoint]
        
        #check if robot has to deliver the EvacuationOrder
        # if houses[checkpoint] not in ["None", 0] and checkpoint not in deliveredOrders:
            # return [0, checkpoint]
        
        #check if robot is loaded
        if loaded_bag != None:
            if loaded_bag in houses:
                bagDistance = Gameboard.getDistance(checkpoint, houses.index(loaded_bag))
        if loaded_brick != None:
            if loaded_brick in humans:
                brickDistance = Gameboard.getDistance(checkpoint, humans.index(loaded_brick))

        #return which item to put down
        if bagDistance != 3 or brickDistance != 3:
            if brickDistance <= bagDistance:
                return [2, humans.index(loaded_brick)]
            else:
                return [1, houses.index(loaded_bag)]

        m_possibilities = []
        #check for scanning
        if 0 in bags:
            if 0 in bricks:
                #check for matches (location to scan both)
                for i in range(len(bags)):
                    if(bricks[i] == 0):
                        m_possibilities.append(i)
                #check for männlidriver possibility
                for possibility in m_possibilities:
                    for house in house_positions:
                        if Gameboard.getDistance(house, possibility) == 1:
                            return [4, house]

        #check if the robot has to scan the human at the position
        if houses[checkpoint] not in ["None", 0] and humans[checkpoint] == 0:
            return [5, checkpoint]
        
        #check to scan a house
        if 0 in houses:
            positions = []
            distances = [3, 3, 3, 3]
            for i in range(4):
                if(houses[i] == 0):
                    positions.append(i)
                    distances[i] = Gameboard.getDistance(checkpoint,i)

            if len(positions) != 0:
                return 3, distances.index(min(distances))

        #check to get sand bags
        if len(deliveredBags) < 2 or len(deliveredBlocks) < 2:
            todoBags = []
            todoBlocks = []
            mWithout_possibilities = []
            mPickup_possibilities = []
            for i in range(4):
                if bags[i] in ["Green", "Blue"] and bags[i] not in deliveredBags and bags[i] in houses:
                    todoBags.append(i)
                if bricks[i] in ["Yellow", "Red"] and bricks[i] not in deliveredBlocks and bricks[i] in humans:
                    todoBlocks.append(i)
            for i in range(4):
                if i in todoBlocks and bricks[i] not in Gameboard.bricksArranged:
                    mWithout_possibilities.append(i)
            for i in range(4):
                if i in todoBags and i in todoBlocks:
                    mPickup_possibilities.append(i)
            
            for possibility in mWithout_possibilities:
                    for house in house_positions:
                        if Gameboard.getDistance(house, possibility) == 1:
                            return [9, house]
                        
                        
            #check to scan a worst case szenario
            print("Houses" + str(houses.count(0)))
            print("possibilities " + str(mWithout_possibilities))
            if(houses.count(0) == 0):
                for possibility in mWithout_possibilities:
                    for house in house_positions:
                        print("Checked worst case")
                        if Gameboard.getDistance(house, possibility) == 2:
                            return [6, possibility]

            for possibility in mPickup_possibilities:
                    for house in house_positions:
                        if Gameboard.getDistance(house, possibility):
                            return [10, possibility]

            
            if len(todoBlocks) > 0:
                distances = [3, 3, 3, 3]
                for i in range(len(todoBlocks)):
                    distances[todoBlocks[i]] = Gameboard.getDistance(checkpoint, todoBlocks[0])
                if distances.count(3) != 4:
                    return [8, min(distances)]

            if len(todoBags) > 0:
                distances = [3, 3, 3, 3]
                for i in range(len(todoBags)):
                    distances[todoBags[i]] = Gameboard.getDistance(checkpoint, todoBags[0])
                if distances.count(3) != 4:
                    return [7, min(distances)]
            
        #return to drive to r6
        return [11, 6]