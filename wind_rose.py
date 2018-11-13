# -*- coding: utf-8 -*-
"""
Created on Fri Nov 09 18:12:51 2018

@author: zdefne
"""


df=pd.read_csv('D:/Documents/PORTAL/terria/Wind_rose_coordinates.csv')
df['n1']=['LO'+str(lon)for lon in df['lon']]
df['n2']=['_LA'+str(lat)  for lat in df['lat']]
df['name']='wind_rose_'+df['n1']+df['n2']+'.png'
df.to_csv('D:/Documents/PORTAL/terria/wind_rose_coords.csv', columns=['id', 'lon', 'lat', 'name'],index=False)