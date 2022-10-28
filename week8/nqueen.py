'''
Author: Ender-Zhang 102596313+Ender-Zhang@users.noreply.github.com
Date: 2022-10-26 11:35:36
LastEditors: Ender-Zhang 102596313+Ender-Zhang@users.noreply.github.com
LastEditTime: 2022-10-26 11:37:35
FilePath: \algrithm_design-1\week8\nqueen.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np

"""
n皇后问题
"""

class Solution:
    t = 0
    def n_queen(self,start, map):
        s.t += 1
        for i in range(len(map[start])):
            # 按行遍历
            map[start][i] = 1
            if self.check(map):
                if start < len(map) - 1:
                    if not self.n_queen(start + 1, map):
                        map[start][i] = 0
                else:
                    print(map)
                    # 将已成立的结果打印出来
                    map[start][i] = 0
                    # 重置
            else:
                map[start][i] = 0
        return False


    def check(self, map):
        # 用于判断是否有皇后处于同一行/列/斜线上
        line1 = set()
        line2 = set()
        line3 = set()
        line4 = set()
        for i in range(len(map)):
            for j in range(len(map)):
                if map[i][j] == 1:
                    if i in line1:
                        return False
                    if j in line2:
                        return False
                    if i - j in line3:
                        return False
                    if i + j in line4:
                        return False
                    line1.add(i)
                    line2.add(j)
                    line3.add(i - j)
                    line4.add(i + j)
        return True


if __name__ == "__main__":
    n = 8
    # 修改n来实现n皇后
    map = np.zeros([n, n])
    s = Solution()
    s.n_queen(0, map)
    print(s.t)
