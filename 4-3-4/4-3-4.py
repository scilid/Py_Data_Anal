# -*- coding: utf-8 -*-


###############################################################################
#######################       4.3.4 任务实现             #######################
###############################################################################

# 代码 4-48
import pandas as pd
order = pd.read_table('./data/meal_order_info.csv',
      sep = ',',encoding = 'gbk')
order['use_start_time'] = pd.to_datetime(order['use_start_time'])
order['lock_time'] = pd.to_datetime(order['lock_time'])
print('进行转换后订单信息表use_start_time和lock_time的类型为：\n',
      order[['use_start_time','lock_time']].dtypes)


# 代码 4-49
year = [i.year for i in order['lock_time']]## 提取年份信息
month = [i.month for i in order['lock_time']]## 提取月份信息
day = [i.day for i in  order['lock_time']]## 提取日期信息
week = [i.week for i in  order['lock_time']]## 提取周信息
weekday = [i.weekday() for i in  order['lock_time']]##提取星期信息
## 提取星期名称信息
weekname = [i.weekday_name for i in  order['lock_time']]
print('订单详情表中的前5条数据的年份信息为：',year[:5])
print('订单详情表中的前5条数据的月份信息为：',month[:5])
print('订单详情表中的前5条数据的日期信息为：',day[:5])
print('订单详情表中的前5条数据的周信息为：',week[:5])
print('订单详情表中的前5条数据的星期信息为：',weekday[:5])
print('订单详情表中的前5条数据的星期名称信息为：',weekname[:5])



# 代码 4-50
timemin = order['lock_time'].min()
timemax = order['lock_time'].max()
print('订单最早的时间为：',timemin)
print('订单最晚的时间为：',timemax)
print('订单持续的时间为：',timemax-timemin)

chekTime = order['lock_time'] - order['use_start_time']
print('平均点餐时间为：',chekTime.mean())
print('最小点餐时间为：',chekTime.min())
print('最大点餐时间为：',chekTime.max())

