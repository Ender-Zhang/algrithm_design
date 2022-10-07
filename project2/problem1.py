'''
Author: yuchen zhang yuchen.zhang1@ucdconnect.ie
Date: 2022-10-04 19:17:52
LastEditors: Ender-Zhang 2245430790@qq.com
LastEditTime: 2022-10-04 22:45:01
FilePath: \algrithm_design\project2\problem1.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from cmath import inf
from re import I


class Solution:
    def getMaxMatrix(self, matrix0: list[list[int]]) -> list[int]:
        matrix = self.changeMatrix(matrix0)
        # print(matrix)
        m, n = len(matrix), len(matrix[0])
        print(m,n)
        ans = []
        # r1, c1, r2, c2 = [0] * 4
        max_sum = matrix[0][0] # 全局最大和
        # max_sum = 0
        for i in range(m): # 起始行
            total = [0] * n
            for j in range(i, m): # 结束行
                cur_max = 0
                for k in range(n):
                # k = j - i
                    # 其实如果不需要统计坐标的只是寻找最大和的话
                    """
                    根连续的子序列的最大和的题写法是一样的
                    cur_max = max(cur_max, cur_max + total[k])
                    max_sum = max(cur_max, max_sum)
                    
                    只不过这里要求统计左上角和右下角的坐标，所以要使用if else 拆开然后记录行号和列号
                    """

                    total[k] += matrix[j][k]
                    if cur_max > 0: # cur_max + total[k] > cur_max 加了比不加更大
                        cur_max += total[k] # 那就加上去
                    else: # cur_max + total[k] <= cur_max 加了变得更小了
                        cur_max = total[k] # 那就不用加了
                        r1 = i # 更新行起点
                        c1 = k # 更新列起点
                    
                    if (i == 0 and c1 == 1):
                        print(cur_max, r1, c1, j, k)

                    if cur_max == max_sum and abs(j - r1) == abs(k - c1):
                        r2, c2 = j, k
                        ans.append([r1, c1, r2, c2])
                        max_sum = cur_max
                        # print(r1 + 1,c1 + 1)
                        # print(cur_max)

                    if cur_max > max_sum and abs(j - r1) == abs(k - c1): # 如果当前和比全局最大和大了
                        ans = []
                        r2, c2 = j, k # 更新一下行终点和列终点
                        # r2, c2 = min(j, k), min(j,k)
                        max_sum = cur_max # 更新当前和为全局最大和
                        ans.append([r1, c1, r2, c2]) # 更新结果

        return ans
    
    def changeMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == 0):
                    matrix[i][j] = - 1000
        return matrix

s = Solution()
testCase1 = [[1,0,1,0,0],
            [1,0,1,1,1],
            [1,1,1,1,0],
            [1,1,0,1,0]]
testCase2 = [[1,1,1,1,1,1],
            [1,1,1,1,0,0],
            [1,1,1,1,1,1],
            [1,1,1,0,0,0],
            [1,0,1,0,1,1],
            [0,0,1,1,1,1]]
testCase3 = [[1,1,1,0,0],
            [1,1,1,1,0],
            [1,1,0,1,0]]
# testCase1 = [[1,-10,1,-10,-10],
#             [1,-10,1,1,1],
#             [1,1,1,1,-10],
#             [1,1,-10,1,-10]]

# t = s.getMaxMatrix(testCase1)
# for i in t:
#     size = (i[2] - i[0]) + 1
#     print("The size is {size} ".format(size = size))
#     print("The indices is {indices} ".format(indices = (i[0] + 1, i[1] + 1)))

s1 = Solution()
t2 = s1.getMaxMatrix(testCase2)
for i in t2:
    size = (i[2] - i[0]) + 1
    print("The size is {size} ".format(size = size))
    print("The indices is {indices} ".format(indices = (i[0] + 1, i[1] + 1)))

# s2 = Solution()
# t3 = s2.getMaxMatrix(testCase2)
# for i in t3:
#     size = (i[2] - i[0]) + 1
#     print("The size is {size} ".format(size = size))
#     print("The indices is {indices} ".format(indices = (i[0] + 1, i[1] + 1)))
