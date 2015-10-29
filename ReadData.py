__author__ = 'yujianmin'
# -*- coding:utf-8 -*-
import pandas as pd
import os

def GetData(filelocation):
    '''
    objection: try to get the data from filelocation and give a describe(if it is url)
    filelocation : string, means the location of file
    return: list with the data
    '''
    # check the file is exist or not #
    if os.path.exists(filelocation) == False:
        print("输入的路径不存在")
        return -1
    else:
        TrainDataFile = filelocation + "/train.csv"
        StoreInfoDataFile = filelocation + "/store.csv"
        TestDataFile = filelocation + "/test.csv"
        Sample_SubmitFile = filelocation + "/sample_submission.csv"
    if os.path.exists(TrainDataFile):
        TrainData = pd.read_csv(TrainDataFile)
    else:
        print("路径下没有名字为train.csv的训练数据集")
    if os.path.exists(StoreInfoDataFile):
        StoreInfoData = pd.read_csv(StoreInfoDataFile)
    else:
        print("路径下没有名字为store.csv的销售信息数据")
    if os.path.exists(TestDataFile):
        TestData = pd.read_csv(TestDataFile)
    else:
        print("路径下没有名字为test.csv的测试数据集")
    if os.path.exists(Sample_SubmitFile):
        Sample_Submit = pd.read_csv(Sample_SubmitFile)
    else:
        print("路径下没有名字为sample_submission.csv的样例数据集")
  # 数据基本特点描述 #
    print("商店信息的基本特点，如下：")
    print(StoreInfoData.describe())
    print("训练集的基本特点，如下：")
    print(TrainData.describe())
    print("测试集的基本特点，如下：")
    print(TestData.describe())
    print("提交结果的样例")
    print(Sample_Submit.ix[0:5,:])

    result = {'TrainData': TrainData, 'StoreInfoData': StoreInfoData, 'TestData': TestData, 'Sample_Submit': Sample_Submit}
