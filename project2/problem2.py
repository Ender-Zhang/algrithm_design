'''
Author: Ender-Zhang 2245430790@qq.com
Date: 2022-10-04 20:01:26
LastEditors: Ender-Zhang 102596313+Ender-Zhang@users.noreply.github.com
LastEditTime: 2022-10-16 12:30:59
FilePath: \algrithm_design\project2\problem2.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from math import log
from mimetypes import init


class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class SolutionA(object):
    def invertTree(self, root):
		# """
		# :type root: TreeNode
		# :rtype: TreeNode
		# """
		# 递归函数的终止条件，节点为空时返回
        if not root:
            return None
		# 将当前节点的左右子树交换
        root.left,root.right = root.right,root.left
		# 递归交换当前节点的 左子树和右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
		# 函数返回时就表示当前这个节点，以及它的左右子树
		# 都已经交换完了		
        return root

    def transferListToTree(self, nums: list):
        def level(index):
            if index >= len(nums) or nums[index] is None:
                return None
            
            root = TreeNode(nums[index])
            root.left = level(2 * index + 1)
            root.right = level(2 * index + 2)
            return root
        return level(0)

    def transTreeToList(self, root: TreeNode):
        dict_ans, depth = self.transTreeToDict(root)
        ans = []
        for i in dict_ans:
            if dict_ans[i].count(None) == len(dict_ans[i]):
                continue
            ans += dict_ans[i]
        return ans
        
    def transTreeToDict(self, root: TreeNode, n = 0):

        # 如果树为空返回空

        if root is None:return {n: [None]}, n
        dict_output = {}
        dict1, k1 = self.transTreeToDict(root.left, n + 1)
        dict2, k2 = self.transTreeToDict(root.right, n + 1)
        k = max(k1, k2)
        # print("k{k}".format(k = k))
        for i in range(k + 1):
            dict_output[i] = []
        
        dict_output[n] = [root.val]

        for i in dict1:
            # if dict1[i] != []:
            #     tmp = dict_output[i]
            #     if tmp == []:
            #         dict_output[i] = dict1[i]
            #         continue
            #     dict_output[i] = tmp.append(dict1[i])
            dict_output[i] += dict1[i]
        for j in dict2:
            # if dict2[j] != []:
            #     tmp = dict_output[j]
            #     if tmp == []:
            #         dict_output[j] = dict2[j]
            #         continue
            #     dict_output[j] = tmp.append(dict1[j])
            dict_output[j] += dict2[j]
        # output.extend(self.transTreeToList(root.left))
        # output.extend(self.transTreeToList(root.right))
        return dict_output, k

class SolutionB:
    def isMirror(self, root1, root2):
        s = SolutionA()
        root1_m = s.invertTree(root1)
        l1 = s.transTreeToList(root1_m)
        l2 = s.transTreeToList(root2)
        if len(l1) != len(l2):
            return "Not Mirror Image"
        for i in range(len(l1)):
            if (l1[i] != l2[i]):
                return "Not Mirror Image"
        return "Mirror Image"

if __name__ == "__main__":
    # partA
    s = SolutionA()
    s2 = SolutionA()
    testCase1 = [4,2,7,1,3,6,9]
    # ans =  [4,7,2,9,6,3,1]
    testCase2 = [34,24,96,10,None,None,None]
    #  ans = [34,96,24,None,None,None,10]

    ans = s.transTreeToList(s.invertTree(s.transferListToTree(testCase1)))
    ans1 = s2.transTreeToList(s2.invertTree(s2.transferListToTree(testCase2)))
    print("PartA")
    print("Test Case 1: {testcase1}".format( testcase1 = ans))
    print("Test Case 2: {testcase2}".format( testcase2 = ans1))


    # partB
    # partB
    print("PartB")
    s_b = SolutionB()
    testCase1t1 = [1,2,3,4,5,6,7]
    testCase1t2 = [1,3,2,7,6,5,4]
    s_a = SolutionA()
    t1 = s_a.transferListToTree(testCase1t1)
    t2 = s_a.transferListToTree(testCase1t2)
    print("Testcase1: " + s_b.isMirror(t1, t2))

    testCase2t1 = [1,2,2,None,3,None,3]
    testCase2t2 = [1,2,2,3,None,3,None]
    s_a = SolutionA()
    t1 = s_a.transferListToTree(testCase2t1)
    t2 = s_a.transferListToTree(testCase2t2)
    print("Testcase2: " + s_b.isMirror(t1, t2))