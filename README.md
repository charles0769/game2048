# game2048
- 使用Python练手

## 规则：
游戏运行在4*4的方格中，出现两个随机的数字
产生随机数的策略：10%的概率是4,90%的概率是2
用户移动方格(wasd)，方格中的数字按照响应规则进行合并
如果地图有变化（数字移动/数字合并),再产生1个随机数

游戏结束：数字不能合并，也没有空白位置

## 架构
界面视图模块 view
逻辑处理模块 controller
数据模块模块
程序入口模块

## 步骤
1、逻辑处理逻辑
创建游戏核心类GameCoreController
将核心算法粘贴进来
将所有参数改成成员变量
产生新数字
--计算所有空白位置(0的位置)
--随机选择一个位置
--根据概率产生一个数字，存入列表的相应位置
2.界面视图模块
创建游戏核心类对象
调用核心类对象的数字方法
呈现界面
获取用户输入，调用核心类的移动方法
产生数字

