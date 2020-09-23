class Gameboard:
    def __init__(self):
        self.house_c = ""
        self.bricks_c = ""
        self.humans_c = ""
        self.sand_c = ""
        self.houses = [0, 0, 0, 0]
        self.sand = [0, 0, 0, 0]
        self.bricks = [0, 0, 0, 0]
        self.humans = [0, 0, 0, 0]
        self.stage = 0
    
    def update(self):
        #Autofill nones
        if(self.houses.count("Green") + self.houses.count("Blue") == 2 and self.houses.count(0) != 0):
            for i in range(self.houses.count(0)):
                self.houses[self.houses.index(0)] = "None"

        if(self.bricks.count("Yellow") + self.bricks.count("Red") == 2 and self.bricks.count(0) != 0):
            for i in range(self.bricks.count(0)):
                self.bricks[self.bricks.index(0)] = "None"
        
        if(self.humans.count("Yellow") + self.humans.count("Red") == 2 and self.houses.count(0) != 0):
            for i in range(self.bricks.count(0)):
                self.bricks[self.bricks.index(0)] = "None"

        if(self.sand.count("Green") + self.sand.count("Blue") == 2 and self.sand.count(0) != 0):
            for i in range(self.sand.count(0)):
                self.sand[self.sand.index(0)] = "None"

        #Autofill Nones in Bricks and Houses
        if(self.bricks.count("Yellow") + self.bricks.count("Red") != 2 and self.bricks.count("None") < 2):
            for i in range(4):
                if(self.houses[i] in ["Green", "Blue"]):
                    self.bricks[i] = "None"
                    self.sand[i] = "None"
        
        if(self.humans.count("Yellow") + self.humans.count("Red") != 2 and self.humans.count("None") < 2):
            for i in range(4):
                if(self.houses[i] in ["None"]):
                    self.humans[i] = "None"

        #Autofill colors
        if(self.houses.count(0) == 1):
            c = "None"
            if(self.house_c == "Blue"):
                c = "Green"
            else:
                c = "Blue"
            self.houses[self.houses.index(0)] = c
        
        if(self.bricks.count(0) == 1):
            c = "None"
            if(self.bricks_c == "Yellow"):
                c = "Red"
            else:
                c = "Yellow"
            self.bricks[self.bricks.index(0)] = c
        
        if(self.humans.count(0) == 1):
            c = "None"
            if(self.humans_c == "Yellow"):
                c = "Red"
            else:
                c = "Yellow"
            self.bricks[self.humans.index(0)] = c
        
        if(self.sand.count(0) == 1):
            c = "None"
            if(self.sand_c == "Blue"):
                c = "Green"
            else:
                c = "Blue"
            self.sand[self.sand.index(0)] = c
    
    def setBrick(self, position, color):
        self.bricks[position] = color
        if color != "None":
            self.bricks_c = color
        self.update()

    def setHouse(self, position, color):
        self.houses[position] = color
        if color != "None":
            self.house_c = color
        self.update()

    def setHuman(self, position, color):
        self.humans[position] = color
        if color != "None":
            self.humans_c = color
        self.update()

    def setSand(self, position, color):
        self.sand[position] = color
        if color != "None":
            self.sand_c = color
        self.update()




    