#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:53:49 2020

@author: lijiaqiang
"""

from matplotlib import pyplot as plt
import pandas as pd

"""获取csv数据"""
data=pd.read_csv('countries.csv')
#通过判断得到country条件为china的数据
china_fitlet=data.country=='China'
#让数据保存到china_data中区
china_data=data[china_fitlet]


us_fitlet=data.country=='United States'
us_data=data[us_fitlet]

jp_fitlet=data.country=='Japan'
jp_data=data[jp_fitlet]

plt.plot(china_data.year,china_data.population/china_data.population.iloc[0])
plt.plot(us_data.year,us_data.population/us_data.population.iloc[0])
plt.plot(jp_data.year,jp_data.population/jp_data.population.iloc[0])

plt.title('Country Population')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend(['China','US','JP'])
plt.show()
