from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

LOADED_BAGS = None
LOADED_BLOCKS = None

class RobotContainer:
    WHEEL_DIAMETER = 5.5
<<<<<<< Updated upstream
    WHEEL_DISTANCE = 8.4
=======
    WHEEL_DISTANCE = 8.3
    # WHEEL_DISTANCE = 8.3
>>>>>>> Stashed changes
    SPEED = 50
    SLOW_SPEED = 30
    AGGRESSION = 6
    LOW_AGGRESSION = 4
    APPROACH_SPEED = 20
    TURN_SPEED = 20
    SLOW_TURN_SPEED = 10
    LINE = ["Black"]
    BLUELINE = ["Blue", "Green"]
    REDLINE = ["Red", "Yellow"]
<<<<<<< Updated upstream
    LOADED_FACTOR = 1.15
=======
    LOADED_FACTOR = 1.05
>>>>>>> Stashed changes
    @staticmethod 
    def setLoaded(bags, blocks):
        global LOADED_BLOCKS, LOADED_BAGS
        if(bags != 0):
            LOADED_BAGS = bags
        if(blocks != 0):
            LOADED_BLOCKS = blocks
    @staticmethod
    def getLoaded():
        global LOADED_BLOCKS, LOADED_BAGS
        return LOADED_BAGS != None, LOADED_BAGS, LOADED_BLOCKS
    def __init__(self):
        pass