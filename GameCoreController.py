'''
游戏核心逻辑
author:Charles Su
create on 2022-1-3 18:10:21
'''

class GameCoreContrller():
    
    # 4*4数组
    Num_list = []
    
    def __init__(self) -> None:
        pass
    
    # 定义函数：将0元素移动到末尾
def MoveZeroToEnd(self):
    if len(self.Num_list) <= 0:
        return self.Num_list
    for i in self.Num_list:
        if i == 0:
            self.Num_list.remove(i)
            self.Num_list.append(i)
    return self.Num_list

# 定义函数：合并函数
def MergeTheNum(self):
    self.Num_list = self.MoveZeroToEnd(self.Num_list)
    for i in range(len(self.Num_list) - 1):
        if self.Num_list[i] == self.Num_list[i + 1]:
            self.Num_list[i] += self.Num_list[i+1]
            self.Num_list[i+1] = 0
    return self.MoveZeroToEnd(self.Num_list)

# 定义函数：将二维列表打印到控制台
def printDoubleList(self):
    for i in range(len(self.Num_list)):
        for j in range(len(self.Num_list[i])):
            print(self.Num_list[i][j],end=" ")
        print()

# 定义向左移动函数
def LeftMove(self):
    for i in range(len(self.Num_list)):
        self.Num_list[i] = self.MergeTheNum(self.Num_list[i])
    return self.Num_list

# 定义向右移动函数
def RightMove(self):
    for i in range(len(self.Num_list)):
        newList = self.Num_list[i][::-1]
        self.Num_list[i][::-1] = self.MergeTheNum(newList)
    return list

# 定义向上移动函数
def UpMove(self):
    map = []
    for i in range(len(self.Num_list[0])):
        newList = []
        for j in range(len(self.Num_list)):
            newList.append(self.Num_list[j][i])
        newList = self.MergeTheNum(newList)
        map.append(newList)
    return [[row[i] for row in map] for i in range(len(map[0]))]

# 定义向下移动函数
def DownMove(self):
    map = []
    for i in range(len(self.Num_list[0])):
        newList = []
        for j in range(len(self.Num_list)):
            newList.append(self.Num_list[j][i])
        newListR = newList[::-1]
        newList[::-1] = self.MergeTheNum(newListR)
        map.append(newList)
    return [[row[i] for row in map] for i in range(len(map[0]))]