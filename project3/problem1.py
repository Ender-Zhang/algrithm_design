# '''
# Author: Ender-Zhang 102596313+Ender-Zhang@users.noreply.github.com
# Date: 2022-10-27 23:00:28
# LastEditors: Ender-Zhang 102596313+Ender-Zhang@users.noreply.github.com
# LastEditTime: 2022-10-27 23:14:36
# FilePath: \algrithm_design-1\project3\problem1.py
# Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
# '''
# Python3 program for the above approach

# Number of vertices in the graph
# define 4 4

# check if the colored
# graph is safe or not

class Solution:
    result_num = 0
    def isSafe(self, graph, color):

        # check for every edge
        for i in range(6):
            for j in range(i + 1, 6):
                if (graph[i][j] and color[j] == color[i]):
                    return False
        return True

    # /* This function solves the m Coloring
    # problem using recursion. It returns
    # false if the m colours cannot be assigned,
    # otherwise, return true and prints
    # assignments of colours to all vertices.
    # Please note that there may be more than
    # one solutions, this function prints one
    # of the feasible solutions.*/


    def graphColoring(self,graph, m, i, color):

        # if current index reached end
        if (i == 6):

            # if coloring is safe
            if (self.isSafe(graph, color)):

                # Print the solution
                # self.printSolution(color)
                if (self.result_num == 1):
                    self.printSolution(color)
                self.result_num += 1
                # return True
            
            return False

        # Assign each color from 1 to m
        for j in range(1, m + 1):
            color[i] = j

            # Recur of the rest vertices
            if (self.graphColoring(graph, m, i + 1, color)):
                return True
            color[i] = 0
        return False

    # /* A utility function to print solution */


    def printSolution(self, color):
        # print("Solution Exists:" " Following are the assigned colors ")
        for i in range(6):
            print(color[i], end=" ")


# Driver code
if __name__ == '__main__':

# /* Create following graph and
# test whether it is 3 colorable
# (3)---(2)
# | / |
# | / |
# | / |
# (0)---(1)
# */
    graph = [
        [0, 1, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0]
    ]
    m = 3 # Number of colors

    # Initialize all color values as 0.
    # This initialization is needed
    # correct functioning of isSafe()
    color = [0 for i in range(6)]

    # Function call
    s = Solution()
    if (not s.graphColoring(graph, m, 0, color)):
        print("result_num", s.result_num)


