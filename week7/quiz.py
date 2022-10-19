'''
Author: Ender-Zhang 102596313+Ender-Zhang@users.noreply.github.com
Date: 2022-10-19 08:58:16
LastEditors: Ender-Zhang 102596313+Ender-Zhang@users.noreply.github.com
LastEditTime: 2022-10-19 09:40:04
FilePath: \algrithm_design-1\week7\quiz.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# class Vertex(object):
#     def __init__(self,data):
#         self.data = data
#         self.firstEdge = None

# class Edge(object):
#     def __init__(self,adjVex,weight):
#         self.adjVex = adjVex
#         self.next = None
#         self.weight = weight

#!/usr/bin/python
# -*- coding: UTF-8 -*-


class graphList:
    def __init__(self):
        self.dict={}  # 顶点名为键，链表为值，链表中存储其它节点的名称和距离

    def addVertex(self,key):
        self.dict[key]=[]

    # 添加无向边
    def addNoDirectLine(self,start,ends):
        for row in ends:
            key=row[0]

            # 1. 在start的邻接表中追加新的边和权值
            lst=self.dict[start]

            flag=True  # 如果在此顶点的邻接表中找到此节点(已经存在)，flag将变为false,也可以用新的进行更新
            for k in lst:
                if k[0]==key:
                    flag=False

            if flag:
                self.dict[start].append(row) # 在邻接表中添加[顶点名称，距离]

            # 2. 在start顶点对应的key节点的邻接表中追加边和权值
            # lst=self.dict[key]
            # flag=True
            # for k in lst:
            #     if k[0]==start:
            #         flag=False
            # if flag:
            #     weight=row[1]
            #     self.dict[key].append([start,weight])

    # 添加有向边
    def addDirectLine(self,start,ends):
        for row in ends:
            key=row[0]

            # 1.在start的邻接表中追加新的边和权值
            lst=self.dict[start]
            flag=True

            for k in lst:
                if k[0]==key:
                    flag=False

            if flag:
                self.dict[start].append(row)


def main():
    lst=['A','B','C','D','E','F','G']

    v3='D'
    ends3=[['A',1],['C',1],['F',1]]

    v1 = "D"
    ends1 = [["C", 1]]

    v2 = "D"
    ends2 = [["C", 1], ["G", 1]]
    v22 = "C"
    ends22 = [["G", 1]]


    gl=graphList()
    for k in lst:
        gl.addVertex(k)

    # testcase1
    gl.addNoDirectLine(v1,ends1)
    print("Testcase1:")

    res = []
    for key in gl.dict:
        t = len(gl.dict[key])
        res.append([key, t])
    res.sort(key=lambda x: x[1], reverse=True)
    print("The node with largest degree is " + str(res[0][0] + " with degree " + str(res[0][1])))

    for key in gl.dict:
        t = gl.dict[key]
        for k in t:
            # res.append[key, k[0], k[1]]
            print([key, k[0], k[1]])
    # print(res)

    # testcase2
    gl2=graphList()
    for k in lst:
        gl2.addVertex(k)
    gl2.addNoDirectLine(v2,ends2)
    gl2.addNoDirectLine(v22,ends22)
    print("Testcase2:")
    res = []
    # print(gl2.dict)

    for key in gl2.dict:
        t = len(gl2.dict[key])
        res.append([key, t])
    res.sort(key=lambda x: x[1], reverse=True)
    print("The node with largest degree is " + str(res[0][0] + " with degree " + str(res[0][1])))
    
    for key in gl2.dict:
        t = gl2.dict[key]
        for k in t:
            # res.append[key, k[0], k[1]]
            print([key, k[0], k[1]])
    # print(res)

    # testcase3
    gl3=graphList()
    for k in lst:
        gl3.addVertex(k)
    gl3.addNoDirectLine(v3,ends3)
    print("Testcase3:")
    res = []
    # print(gl3.dict)

    for key in gl3.dict:
        t = len(gl3.dict[key])
        res.append([key, t])
    res.sort(key=lambda x: x[1], reverse=True)
    print("The node with largest degree is " + str(res[0][0] + " with degree " + str(res[0][1])))
    
    for key in gl3.dict:
        t = gl3.dict[key]
        for k in t:
            # res.append[key, k[0], k[1]]
            print([key, k[0], k[1]])


if __name__ == '__main__':
    main()


