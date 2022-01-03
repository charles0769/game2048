'''
2048小游戏
author:Charles Su
create on 2022-1-3 11:29:56
'''

# 定义函数：将0元素移动到末尾
def MoveZeroToEnd(list):
    if len(list) <= 0:
        return list
    for i in list:
        if i == 0:
            list.remove(i)
            list.append(i)
    return list

# 定义函数：合并函数
def MergeTheNum(list):
    list = MoveZeroToEnd(list)
    for i in range(len(list) - 1):
        if list[i] == list[i + 1]:
            list[i] += list[i+1]
            list[i+1] = 0
    return MoveZeroToEnd(list)

# 定义函数：将二维列表打印到控制台
def printDoubleList(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j],end=" ")
        print()

# 定义向左移动函数
def LeftMove(list):
    for i in range(len(list)):
        list[i] = MergeTheNum(list[i])
    return list

# 定义向右移动函数
def RightMove(list):
    for i in range(len(list)):
        newList = list[i][::-1]
        list[i][::-1] = MergeTheNum(newList)
    return list

# 定义向上移动函数
def UpMove(list):
    map = []
    for i in range(len(list[0])):
        newList = []
        for j in range(len(list)):
            newList.append(list[j][i])
        newList = MergeTheNum(newList)
        map.append(newList)
    return [[row[i] for row in map] for i in range(len(map[0]))]

# 定义向下移动函数
def DownMove(list):
    map = []
    for i in range(len(list[0])):
        newList = []
        for j in range(len(list)):
            newList.append(list[j][i])
        newListR = newList[::-1]
        newList[::-1] = MergeTheNum(newListR)
        map.append(newList)
    return [[row[i] for row in map] for i in range(len(map[0]))]

if __name__ == "__main__":
    a=[[4,2,2,2],[0,2,0,2]]
    #printDoubleList(LeftMove(a))
    #printDoubleList(RightMove(a))
    #printDoubleList(UpMove(a))
    printDoubleList(DownMove(a))
    
    '''
    4 2 2 2 ->>> 4 4 2 0 
    0 2 0 2 ->>> 4 0 0 0
    
    4 2 2 2 ->>> 0 4 2 4 
    0 2 0 2 ->>> 0 0 0 4
    
    4 2 2 2 ->>> 4 4 2 4 
    0 2 0 2 ->>> 0 0 0 0
    
    4 2 2 2 ->>> 0 0 0 0
    0 2 0 2 ->>> 4 4 2 4
    '''