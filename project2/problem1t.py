'''
Author: Ender-Zhang 2245430790@qq.com
Date: 2022-10-04 21:38:52
LastEditors: Ender-Zhang 2245430790@qq.com
LastEditTime: 2022-10-05 22:09:53
FilePath: \algrithm_design\project2\problem1t.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# '''
# Author: Ender-Zhang 2245430790@qq.com
# Date: 2022-10-04 21:38:52
# LastEditors: Ender-Zhang 2245430790@qq.com
# LastEditTime: 2022-10-04 21:42:01
# FilePath: \algrithm_design\project2\problem1'.py
# Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
# '''



class Solution(object):
 
    def getMaxMatrix(self, matrix0):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        matrix = self.changeMatrix(matrix0)
        # for i in matrix:
        #     print(i)
        row, col = len(matrix), len(matrix[0]) if matrix else 0
        max_sum = float('-inf')
        level_sum = [0] * col
        x1 = y1 = x2 = y2 = 0
        c1 = 0
        ans = []
        for i in range(row):
            #每层都重新统计前序和
            for w in range(col):
                level_sum[w] = 0

           
            for j in range(i, row):
                sub_sum = 0
                for k in range(col):
                    level_sum[k] += matrix[j][k]
                    if sub_sum <= 0:
                        sub_sum = level_sum[k]
                        c1 = k
                    else:
                        sub_sum += level_sum[k]

                    # if i == 0 and j == 2:
                    #     print(level_sum,k,sub_sum)

                    # if i == 0 and c1 == 1 and j == 2 and k == 3:
                    #     print("111111111")
                    if sub_sum == max_sum:
                        max_sum = sub_sum
                        x1 = i 
                        y1 = c1
                        x2 = j
                        y2 = k
                        ans.append([i,c1,j,k])
                        
                    if sub_sum > max_sum and j - i == k - c1:
                        max_sum = sub_sum
                        x1 = i 
                        y1 = c1
                        x2 = j
                        y2 = k
                        ans = [[i,c1,j,k]]
                        # ans.append([i,c1,j,k])
        return ans

    def changeMatrix(self, matrix):
        # print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == 0):
                    matrix[i][j] = - 1000
        return matrix

    def reverseMatrix(self, matrix):
        ans = [[0 for c_ in range(len(matrix))] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                ans[i][j] = matrix[j][i]
        return ans

    def getReverseAnswer(self, ans2):
        for i in ans2:
            tmp = i[0]
            i[0] = i[1]
            i[1] = tmp
            tmp = i[2]
            i[2] = i[3]
            i[3] = tmp
        return ans2

    def integrateAnswer(self, ans1, ans2):
        l = []
        for i in ans1:
            for j in ans2:
                if (i == j):
                    ans2.remove(j)
        l = ans1 + ans2
        return l
    def getAnswer(self,matrix):
        ans1 = self.getMaxMatrix(matrix)
        ans2 = self.getReverseAnswer(self.getMaxMatrix(self.reverseMatrix(matrix)))
        return self.integrateAnswer(ans1,ans2)





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
             
testCase3 = [[1,1,1,0,1,1],
             [1,1,1,0,0,0],
             [1,1,1,0,0,0],
             [1,0,0,1,1,1],
             [1,0,1,1,1,1],
             [1,0,1,1,1,1],
             [0,0,1,1,1,1]]
s = Solution()
t = s.getAnswer(testCase2)
print(t)

