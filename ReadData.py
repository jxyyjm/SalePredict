__author__ = 'yujianmin'
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import os

def ReadData(filelocation):
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
        print("训练集的大小：")
        print(np.shape(TrainData))
    else:
        print("路径下没有名字为train.csv的训练数据集")
        print(TrainDataFile)
    if os.path.exists(StoreInfoDataFile):
        StoreInfoData = pd.read_csv(StoreInfoDataFile)
        print("商店信息集的大小：")
        print(np.shape(StoreInfoData))
    else:
        print("路径下没有名字为store.csv的销售信息数据")
        print(StoreInfoDataFile)
    if os.path.exists(TestDataFile):
        TestData = pd.read_csv(TestDataFile)
        print("测试集的大小：")
        print(np.shape(TestData))
    else:
        print("路径下没有名字为test.csv的测试数据集")
        print(TestDataFile)
    if os.path.exists(Sample_SubmitFile):
        Sample_SubmitData = pd.read_csv(Sample_SubmitFile)
        print("提交样例的大小：")
        print(np.shape(Sample_SubmitData))
    else:
        print("路径下没有名字为sample_submission.csv的样例数据集")
        print(Sample_SubmitFile)
    # 数据基本特点描述 #
    print("商店信息的基本特点，如下：")
    print(StoreInfoData.describe())
    print("训练集的基本特点，如下：")
    print(TrainData.describe())
    print("测试集的基本特点，如下：")
    print(TestData.describe())
    print("提交结果的样例")
    print(Sample_SubmitData.ix[0:5,:])

    result = {'TrainData': TrainData, 'StoreInfoData': StoreInfoData, 'TestData': TestData, 'Sample_SubmitData': Sample_SubmitData}
    return result
