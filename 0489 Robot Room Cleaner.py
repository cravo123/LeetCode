# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def dfs(self, robot, i, j, di, dj, seen):
        robot.clean()
        seen.add((i, j))
        
        for _ in range(4):
            if (i + di, j + dj) not in seen and robot.move():
                self.dfs(robot, i + di, j + dj, di, dj, seen)
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            di, dj = -dj, di
            robot.turnLeft()
        
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        seen = set()
        
        self.dfs(robot, 0, 0, -1, 0, seen)
        
        