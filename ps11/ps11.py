# Problem Set 11: Simulating robots
# Name:
# Collaborators:
# Time:

import math
import random
import ps11_visualize
import pylab
import matplotlib.pyplot as plt



# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)


# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        # TODO: Your code goes here
        self.tiles ={}
        for i in range(self.width):
            for j in range(self.height):
                self.tiles[(i,j)] = 0
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # TODO: Your code goes here
        intx = int(pos.getX())
        inty = int(pos.getY())
        self.tiles[(intx,inty)] = 1
                                
        
        
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tiles[(m,n)]
        
        # TODO: Your code goes here
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.height*self.width 
        # TODO: Your code goes here
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        temp = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.tiles[i,j] == 1:
                    temp += 1
        #print temp
        return temp
        # TODO: Your code goes here
    def getRandomPosition(self):
        """
        Return a random position inside the room.
        
        returns: a Position object.
        """
        a = random.uniform(0,self.width)
        b = random.uniform(0,self.height)
        return (Position(a,b))
        # TODO: Your code goes here
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        if pos.x <= self.width and pos.y <= self.height:
            if pos.x >=0 and pos.y >=0 :
                return 1
       
        return 0
        # TODO: Your code goes here


class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        
        self.room = room
        self.speed = speed
        self.direction = random.uniform(0,360)
        self.position = Position(random.uniform(0,room.width),random.uniform(0,room.height))
        
        # TODO: Your code goes here
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
        # TODO: Your code goes here
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction
    
        # TODO: Your code goes here
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        
        self.position = position
        
        # TODO: Your code goes here
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction
        # TODO: Your code goes here


class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        oldposition = self.getRobotPosition()
        #print '0'
        newposition = oldposition.getNewPosition(self.getRobotDirection(),self.speed)
        #print '0.5'
        while self.room.isPositionInRoom(newposition) == 0 :
            #print '1'
            self.setRobotDirection(random.uniform(0,360))
            #print '2'
            newposition = oldposition.getNewPosition(self.getRobotDirection(),self.speed)
            #print '3'
        self.setRobotPosition(newposition)
        #print '4'
        self.room.cleanTileAtPosition(newposition)
        #print '5'
        # TODO: Your code goes here
        


# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """
    # TODO: Your code goes here
    

    
#    for robot in listofrobots:
#        robot.setRobotPosition(theroom.getRandomPosition())
#    for robots in listofrobots:
#                assert type(robots) == Robot
#                robots.updatePositionAndClean()
#    anim.update(theroom, listofrobots)
                
    
    count =0
    while num_trials > count:
        listoflists = []
        theroom = RectangularRoom(width,height)
        listofrobots=[]
        for i in range(num_robots):
            listofrobots.append(robot_type(theroom,speed))
        lists = []
        coverage = 0
        if visualize == True:
            anim = ps11_visualize.RobotVisualization(num_robots, width, height)
        for robot in listofrobots:
            robot.setRobotPosition(theroom.getRandomPosition())
        while coverage < min_coverage:
            for robots in listofrobots:
                robots.updatePositionAndClean()
            if visualize == True:
                anim.update(theroom, listofrobots)
            coverage = float(theroom.getNumCleanedTiles())/theroom.getNumTiles()
            lists.append(coverage)
            
        
        
        
        
        
        count += 1
        listoflists.append(lists)
    if visualize == True:
        anim.done()
    return listoflists
#avg = runSimulation(10, 1.0, 10, 15, 0.8, 30, Robot, False)
# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means




# === Problem 4
def avelength(listoflists):
    sumup = sum((len(lists))for lists in listoflists)
    return sumup / len(listoflists)    
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    # TODO: Your code goes here
    roomsize=[5,10,15,20,25]
    sims=[]
    sims.append(avelength(runSimulation(1, 1.0, 5, 5, 0.75, 10, Robot, False)))
    sims.append(avelength(runSimulation(1, 1.0, 10, 10, 0.75, 10, Robot, False)))
    sims.append(avelength(runSimulation(1, 1.0, 15, 15, 0.75, 10, Robot, False)))
    sims.append(avelength(runSimulation(1, 1.0, 20, 20, 0.75, 10, Robot, False)))
    sims.append(avelength(runSimulation(1, 1.0, 25, 25, 0.75, 10, Robot, False)))
    
    roomsize=[5,10,15,20,25]
    pylab.plot(roomsize,sims)
    plt.xlabel('Room Size x*x')
    plt.ylabel('Time')
    plt.title('Average time taken for a robot to clean 75% of the room')
        

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    sims=[]
    robots=[]
    for nrobots in range(1,11):
        robots.append(nrobots)
        sims.append(avelength(runSimulation( nrobots , 1.0, 25, 25, 0.75, 10, Robot, False)))
        print nrobots
    
    pylab.plot(robots,sims)
    plt.xlabel('number of robots')
    plt.ylabel('Time')
    plt.title('Average time taken for n robot to clean 75% of the room')
    # TODO: Your code goes here

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    # TODO: Your code goes here
    #How long does it take two robots to clean 75% of rooms with dimensions 20x20, 25x16, 40x10, 50x8, 80x5, and 100x4?
    ratios=[1,25.0/16,4,50.0/8,16,25]
    sims=[]
    sims.append(avelength(runSimulation(2, 1.0, 20, 20, 0.75, 10, Robot, False)))
    
    sims.append(avelength(runSimulation(2, 1.0, 25, 16, 0.75, 10, Robot, False)))

    sims.append(avelength(runSimulation(2, 1.0, 40, 10, 0.75, 10, Robot, False)))
    sims.append(avelength(runSimulation(2, 1.0, 50, 8, 0.75, 10, Robot, False)))
    sims.append(avelength(runSimulation(2, 1.0, 80, 5, 0.75, 10, Robot, False)))
    sims.append(avelength(runSimulation(2, 1.0, 100, 4, 0.75, 10, Robot, False)))
    pylab.plot(ratios,sims)
    plt.xlabel('ratios of width/height')
    plt.ylabel('Time')
    plt.title('Average time taken for 2 robot to clean 75% of different room')
    
    

def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    # TODO: Your code goes here]
    coverages=[]
    robots=[]
    
    for n in range(1,6):
        coverages.append(computeMeans(runSimulation(n, 1.0, 25, 25, 0.75, 10, Robot, False)))
    for i in range(5):
        robots.append(list(range(len(coverages[i]))))
    for i in range(5):
        pylab.plot(coverages[i],robots[i], label=' %i robot'%(i+1))
    plt.xlabel('coverages')
    plt.ylabel('Time')
    plt.title('Average time taken for n robot to clean x% of different room')
    plt.legend()


# === Problem 5
#    ,coverages[1],robots[1],label='two robots',coverages[2],robots[2],label='three robots',coverages[3],robots[3],label ='four robots',coverages[4],robots[4],label = 'five robots'

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    
    """
    def updatePositionAndClean(self):
        oldposition = self.getRobotPosition()
        #print '0'
        self.setRobotDirection(random.uniform(0,360))
            #print '2'
        newposition = oldposition.getNewPosition(self.getRobotDirection() , self.speed)
        #print '0.5'
        while self.room.isPositionInRoom(newposition) == 0 :
            #print '1'
            self.setRobotDirection(random.uniform(0,360))
            #print '2'
            newposition=oldposition.getNewPosition(self.getRobotDirection(),self.speed)
            #print '3'
        self.setRobotPosition(newposition)
        #print '4'
        self.room.cleanTileAtPosition(newposition)



# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    # TODO: Your code goes here
    roomsize=[5,10,15,20,25]
    sims=[]
    sims1=[]
    sims.append(avelength(runSimulation(1, 1.0, 5, 5, 0.75, 10, Robot, False)))
    sims.append(avelength(runSimulation(1, 1.0, 10, 10, 0.75, 10, Robot, False)))
    sims.append(avelength(runSimulation(1, 1.0, 15, 15, 0.75, 10, Robot, False)))
    sims.append(avelength(runSimulation(1, 1.0, 20, 20, 0.75, 10, Robot, False)))
    sims.append(avelength(runSimulation(1, 1.0, 25, 25, 0.75, 10, Robot, False)))
    
    sims1.append(avelength(runSimulation(1, 1.0, 5, 5, 0.75, 10, RandomWalkRobot, False)))
    sims1.append(avelength(runSimulation(1, 1.0, 10, 10, 0.75, 10, RandomWalkRobot, False)))
    sims1.append(avelength(runSimulation(1, 1.0, 15, 15, 0.75, 10, RandomWalkRobot, False)))
    sims1.append(avelength(runSimulation(1, 1.0, 20, 20, 0.75, 10, RandomWalkRobot, False)))
    sims1.append(avelength(runSimulation(1, 1.0, 25, 25, 0.75, 10, RandomWalkRobot, False)))

    
    roomsize=[5,10,15,20,25]
    pylab.plot(roomsize,sims,label='Normal robot')
    pylab.plot(roomsize,sims1,label='RandomWalkRobot')
    plt.xlabel('Room Size x*x')
    plt.ylabel('Time')
    plt.title('Average time taken for a robot to clean 75% of the room')
    plt.legend()
    plt.show()


#runSimulation(1, 1.0, 15, 15, 0.75, 10, RandomWalkRobot, True)
#runSimulation(10,3,20,20,0.9,2,RandomWalkRobot,True)
