# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:48:37 2023

@author: User
"""
height=float(input("請輸入你的身高(公尺)"))
weight=float(input("請輸入你的體重(公斤)"))

BMI=weight/(height**2)

print(f"你的BMI是{BMI:.2f}")
