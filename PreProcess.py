__author__ = 'yujianmin'
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import datetime

# 数据清理 和 合并 #
Class DataProcess(TrainData, StoreInfoData):
    '''
    objection : 数据预处理
    TrainData : DataFrame, 包含训练数据
    StoreInfoData : DataFrame, 包含店面的各项信息
    Function:
    （1）Merge(TrainData, StoreInfoData)
             #按照StoreID将StoreInfoData与TrainData合并
    （2）Promo2Duration(NewTrainData)
              #按照数据的提取时间Date，促销开始年份Promo2SinceYear，促销季节PromoInterval, 计算促销的历史积累时间
    （3）AddNewColumns(NewTrainData)
             #增加属性，按照Date，增加所处销售月份SaleMonth，所处销售季节SaleSeason，销售年份SaleYear
    '''
    def __init__(self, TrainData, StoreInfoData):
        self.TrainData = TrainData
        self.StoreInfoData = StoreInfoData
        self.NewTrainData = 0
    def __del__(self):
        pass
    def Say(self):
        print("调用此类的AllProcess函数，会依次执行合并操作，是否促销判断，促销时长计算，增加新列，字符转换")
        print("也可以单独调用某个函数，请参考源码，自行修改")
    def AllProcess(self):
        # 所有预处理均在此处执行一遍，并返回整理好的结果 #
        self.Merge()
        self.Promo2Duration()
        self.AddNewColumns()
        self.TransLetter()
        return self.NewTrainData
    def Merge(self):
        #按照StoreID将StoreInfoData与TrainData合并
        self.NewTrainData = pd.merge(self.TrainData, self.StoreInfoData, how = 'left', on = ['Store'])
        print("合并数据have been done ...")
    def Promo2Duration(self):
        #按照数据的提取时间Date，促销开始年份Promo2SinceYear，促销季节PromoInterval，计算促销历史积累时间
        #self.NewTrainData['Date']
        #self.NewTrainData['Promo2SinceYear']
        #self.NewTrainData['PromoInterval']
        if 'Promo2Duration' in list(slef.NewTrainData.columns()):
            pass
        else:
            add = pd.DataFrame(np.zeros((np.shape(self.NewTrainData)[0], 1)), columns = ['Promo2Duration'])
            self.NewTrainData = pd.concat([self.NewTrainData, add], axis=1) # 按列添加 #
        # update the col named 'Promo2Duration' #
        # here is import !!! #

        print("计算当天的历史累计促销时长have been done ... ")
    def AddNewColumns(self):
        #增加属性，按照Date，增加所处销售月份SaleMonth，所处销售季节SaleSeason，销售年份SaleYear
        # check 检查是否已经有了新的属性
        columnNames = self.NewTrainData.columns()
        columnNames = list(columnNames)
        CheckColName = ['SaleMonth', 'SaleSeason', 'SaleYear']
        for i in range(len(CheckColName)):
            name = CheckColName[i]
            if name in columnNames:
                pass
            else:
                add = pd.DataFrame(np.zeros((np.shape(self.NewTrainData)[0], 1)), columns = [name])
                self.NewTrainData = pd.concat([self.NewTrainData, add], axis=1) # 按列添加 #
        # 对这三个属性 更新值
        Date = self.NewTrainData['Date']
        Date = pd.to_datetime(Date)
        for i range(len(Date)):
            self.NewTrainData['SaleMonth'] = Date[i].month
            self.NewTrainData['SaleSeason'] = Date[i].month/3 + 1
            self.NewTrainData['SaleYear'] = Date[i].year
        print("增加三个属性SaleMonth, SaleSeason, SaleYear have been done ...")
    def TransLetter(self):
        # 将字符表示转换为数字表示 #
        # （1）StoreType 四种店模式 a => 1, b => 2, c => 3, d => 4
        # （2）Assortment 描述种类 a:basic => 1, b:extra => 2, c:extend => 3
        #（3）StateHoliday 节假日说明 a：公共节假日 => 1, b：复活节 =>2, c：圣诞节 => 3, 0:none => None
        #（4）其他的还没有想到
        self.NewTrainData['StoreType'].replace(['a', 'b', 'c', 'd'], [1, 2, 3, ,4])
        self.NewTrainData['Assortment'].replace(['a', 'b', 'c'], [1, 2, 3])
        self.NewTrainData['StateHoliday'].replace(['a', 'b', 'c'], [1, 2, 3])
        print("字符转换have been done ...")
def __name__=="__main__":
    TrainData = 0
    StoreInfoData = 0
    CPreProcess = DataProcess(TrainData, StoreInfoData)
    CPreProcess.Say()