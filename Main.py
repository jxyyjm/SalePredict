__author__ = 'yujianmin'
# -*- coding:utf-8 -*-
# here try to together all the model and give an simple and clear view #
from ReadData import ReadData
from PreProcess import PreProcess
import PredictModel

import numpy as np
import pandas as pd

# read the data #
filelocation = "/home/yujianmin/下载/AKaggleData"
AllData = ReadData(filelocation)
TrainData = AllData['TrainData']
StoreInfoData = AllData['StoreInfoData']
TestData = AllData['TestData']
Sample_SubmitData = AllData['Sample_SubmitData']

print(np.shape(TrainData))


# data pre-process #
CPreProcess = PreProcess(TrainData, StoreInfoData)
NewData = CPreProcess.AllProcess()
#
