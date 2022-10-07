'''
Author: Ender-Zhang 2245430790@qq.com
Date: 2022-10-05 22:15:54
LastEditors: Ender-Zhang 2245430790@qq.com
LastEditTime: 2022-10-06 08:35:48
FilePath: \algrithm_design\project2\problem3.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from scipy.optimize import linear_sum_assignment
import numpy as np
 
cost = np.array([[0.64, 1.63, 3.95, 4.09, 4.48],
                 [3.95, 4.48, 0.73, 0.23, 2.26],
                 [0.42, 0.70, 4.24, 4.56, 4.35],
                 [3.73, 3.84, 1.07, 1.95, 0.85],
                 [4.37, 5.02, 1.60, 0.73, 3.48]])
                 
row_ind, col_ind = linear_sum_assignment(cost)
print('row_ind:', row_ind)  # 开销矩阵对应的行索引
print('col_ind:', col_ind)  # 对应行索引的最优指派的列索引
print('cost:', cost[row_ind, col_ind])  # 提取每个行索引的最优指派列索引所在的元素，形成数组
print('cost_sum:', cost[row_ind, col_ind].sum())  # 最小开销