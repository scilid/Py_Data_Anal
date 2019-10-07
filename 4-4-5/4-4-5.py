# -*- coding: utf-8 -*-

###############################################################################
#######################            任务实现             #######################
###############################################################################

# 代码 4-64
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://mytest:1234@127.0.0.1:\
3306/testdb?charset=utf8mb4')
detail = pd.read_sql_table('meal_order_detail1', con=engine)
detail['place_order_time'] = pd.to_datetime(
    detail['place_order_time'])
detail['date'] = [i.date() for i in detail['place_order_time']]
detailGroup = detail[['date', 'counts', 'amounts']].groupby(by='date')
print('订单详情表前5组每组的数目为：\n', detailGroup.size().head())

# 代码 4-65
dayMean = detailGroup.agg({'amounts': np.mean})
print('订单详情表前五组每日菜品均价为：\n', dayMean.head())

dayMedian = detailGroup.agg({'amounts': np.median})
print('订单详情表前五组每日菜品售价中位数为：\n', dayMedian.head())

# 代码 4-66
daySaleSum = detailGroup.apply(np.sum)['counts']
print('订单详情表前五组每日菜品售出数目为：\n', daySaleSum.head())
